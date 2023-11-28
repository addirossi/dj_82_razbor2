"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from main.views import cars_list, CreateCarView, CarsListView, SaleDetails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/cars/', CarsListView.as_view()),
    path('api/v1/cars/create/', CreateCarView.as_view()),
    path('api/v1/sales/<int:pk>/', SaleDetails.as_view())
]
