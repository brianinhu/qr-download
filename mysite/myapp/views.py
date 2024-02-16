import qrcode
import base64
from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponse
import os


def descargar_excel(request, nombre_archivo):
    # Ruta del archivo
    ruta_archivo = os.path.join('media', nombre_archivo)
    
    # Verifica si el archivo existe
    if not os.path.exists(ruta_archivo):
        return HttpResponse("El archivo no existe", status=404)

    # Abre el archivo y devuelve una respuesta de archivo
    with open(ruta_archivo, 'rb') as archivo:
        response = HttpResponse(archivo.read(
        ), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="{
            nombre_archivo}"'
        return response


def index(request):
    nombre_archivo = 'planilla.xlsx'

    # URL de descarga del archivo
    url_descarga = request.build_absolute_uri(
        # Ingresar la direccion IPv4 de la maquina que aloja el servidor
        f'http://0.0.0.0:8000/descargar_excel/{nombre_archivo}')

    # Creando el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    # Agregando la data al QR, en este caso la URL de la página de descarga
    qr.add_data(url_descarga)
    qr.make(fit=True)

    # Creando la imagen del QR
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Creando un buffer para guardar la imagen
    qr_img_buffer = BytesIO()

    # Guardando la imagen en el buffer
    qr_img.save(qr_img_buffer)

    # Moviendo el cursor del buffer al inicio
    qr_img_buffer.seek(0)

    # Convirtiendo la imagen a base64
    qr_img_base64 = base64.b64encode(qr_img_buffer.read()).decode("utf-8")

    # Mostrando el QR en el navegador
    return render(request, 'index.html', {'qr_img': qr_img_base64})
