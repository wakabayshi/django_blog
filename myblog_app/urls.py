from django.contrib import admin
from django.urls import path 
from . import views #追加


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]