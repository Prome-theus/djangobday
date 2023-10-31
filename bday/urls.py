from django.contrib import admin
from django.urls import path
from bday import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.main,name='main'),
    path('main/',views.Homepage,name='home')
]