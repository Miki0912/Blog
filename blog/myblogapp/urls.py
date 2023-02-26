from django.urls import path
from .views import HomeView, PostDetailView

app_name = 'myblogapp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', PostDetailView.as_view(), name='post-detail'),

]