from django.urls import path
from myblogapp import views

app_name = 'myblogapp'

urlpatterns = [
    path('', views.home, name='home'),

]