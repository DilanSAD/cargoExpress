# cargoExpress
Este proyecto gestiona y registra pedidos entregados utilizando una API REST. Los datos se almacenan en una base de datos y se exponen a través de un API Gateway. Utiliza Python para el procesamiento del backend, LocalStack para emular los servicios de AWS, y Lambda Functions para manejar las operaciones de registro.

# Requisitos previos:
-	Instalar WSL con Ubuntu https://learn.microsoft.com/es-es/windows/wsl/install 
-	Instalar Docker (Desktop personal para mejor experiencia) https://docs.docker.com/get-started/introduction/get-docker-desktop/

# Preparación para la ejecución del proyecto

## 1 :
Ejecuta El script ejecutar.sh para crear y preparar el entorno virtual.

Al ejecutar el script se puede dar como argumento un nombre para el entorno virtual si no se indica tomara venv por defecto.  Este script crea, activa, configura e instala las dependencias necesarias para el proyecto desde requirements.txt en el entorno virtual, en si este script Proporciona un entorno preparado para la ejecución y despliegue del proyecto usando LocalStack.

## 2:
Activa el entorno virtual (esto depende del shell que estés usando)
Ejemplos de comandos
  cmd
    venv\Scripts\activate
    venv\Scripts\deactivate
  bash
    source venv/Scripts/activate
    deactivate
Una vez activo el entorno virtual, se pueden usar comandos de awslocal y LocalStack dentro del entorno.

## 3:
Ingresar a la ruta de /cloudformation y ejecutar el script desplegar.sh este script se encarga de establecer las credenciales de AWS para el entorno. Luego, inicia el contenedor de LocalStack con docker-compose.yml, El script crea un bucket S3 en LocalStack y copia los archivos .zip de las funciones Lambda al volumen compartido. Estos archivos se cargan en el bucket S3. para acto seguido desplegar el stack de CloudFormation usando el archivo template.yml para crear y configurar los recursos necesarios en el proyecto.

Con los 2 arteriores script del paso 1 y 3 preparamos el entorno y desplegamos los recursos.

## 4:
Por ultimo se debe ingresar a la ruta de src/script y ejecutar el archivo script.py apoyandose en python, este archivo se encarga de registrar los datos en la tabla de Entregas
