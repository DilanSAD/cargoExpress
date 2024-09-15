#!/bin/bash

# Configurar variables de entorno para LocalStack
export AWS_ACCESS_KEY_ID=test
export AWS_SECRET_ACCESS_KEY=test
export AWS_DEFAULT_REGION=us-east-1

# Iniciar el contenedor de localstack
echo " --- Iniciando el contenedor de LocalStack"
docker-compose up -d
# Espera un momento para que los los servicios de LocalStack se inicien
sleep 10

# Crea el bucket en LocalStack (si no existe ya)
echo " --- Creando el bucket S3 en LocalStack"
awslocal --endpoint-url=http://localhost:4566 s3 mb s3://my-bucket

# Copia los archivos .zip al volumen compartido
echo " --- Copiando archivos .zip al volumen compartido"
cp ../src/entregas/infrastructure/entregas.zip volume/entregas.zip
cp ../src/monitoreo/infrastructure/monitoreo.zip volume/monitoreo.zip

# Carga el archivo .zip al bucket S3
echo " --- Cargando archivos .zip al bucket S3"
awslocal --endpoint-url=http://localhost:4566 s3 cp volume/entregas.zip s3://my-bucket/entregas.zip
awslocal --endpoint-url=http://localhost:4566 s3 cp volume/monitoreo.zip s3://my-bucket/monitoreo.zip



# Desplegar el stack de CloudFormation
echo " --- Desplegando stack de CloudFormation..."
awslocal cloudformation create-stack \
    --stack-name cargo-express-stack \
    --template-body file://template.yml \
    --capabilities CAPABILITY_IAM

# Esperar a que el stack se complete
echo " --- Esperando a que el stack se complete..."
awslocal cloudformation wait stack-create-complete --stack-name cargo-express-stack
echo " --- Despliegue completado"
