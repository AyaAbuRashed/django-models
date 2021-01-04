from django.urls import path, include
from .views import HomeView, BlogDetailesView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', BlogDetailesView.as_view(), name='blog_details'),
]