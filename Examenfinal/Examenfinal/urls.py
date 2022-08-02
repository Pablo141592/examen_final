"""Examenfinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),
    path('cursos/', views.index, name = "cursos"),
    path('crearcurso/', views.crearcurso, name = "crearcurso"),
    path('carreras/', views.carreras, name = "carreras"),
    path('crearcarrera/', views.crearcarrera, name = "crearcarrera"),
    path('listar_course/',views.listar_course,name="listar_course"),
    path('eliminar_course/<int:id>',views.eliminar_course, name='eliminar_course'),
    path('create_course/',views.create_course, name='create_course'),
]