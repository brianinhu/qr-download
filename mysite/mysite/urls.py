from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Pantalla principal del proyecto (QR)
    path('', views.index, name='index'),
    # Descargar el archivo excel
    path('descargar_excel/<str:nombre_archivo>', views.descargar_excel, name='descargar_excel')
]
