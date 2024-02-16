# Descarga de archivo con QR y botón

## Descripción
Este proyecto muestra cómo descargar un archivo excel (.xlsx) con un QR generado con la librería qrcode y un botón. Además, se implementa un servidor local mediante el wifi de la computadora para que otros dispositivos puedan acceder a la página y descargar el archivo.

## Pasos
1. Clonar el repositorio.
2. Instalar las dependencias con `pip install -r requirements.txt`.
3. Abrir el archivo `views.py` y cambiar la dirección IP en la línea 32 por la dirección IP de la computadora.
4. Abrir la terminal (ctrl + ñ) e ir al directorio ..\qr-planilla\mysite con el comando `cd .\mysite\`.
5. Ejecutar el comando `py manage.py runserver 0.0.0.0:8000`.
6. Ingresar en el navegador la dirección `http://127.0.0.1:8000/` para ver la página.
7. Ingresar en el navegador de otro dispositivo la dirección `http://<dirección IP de la computadora>:8000/` para ver la página.

## Resultados

- ### Desktop

<img src="mysite/media/desktop.png" alt="Logo de Markdown" width="600">

- ### Mobile

<img src="mysite/media/mobile.png" alt="Logo de Markdown" width="200">