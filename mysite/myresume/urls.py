from django.urls import path

from myresume import views

app_name = 'myresume'

urlpatterns = [
    path('', views.index, name='index'),
]