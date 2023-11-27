from django.contrib import admin
from django.urls import path
from django.urls import include
from rango import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('rango/', include('rango.urls')),
]
