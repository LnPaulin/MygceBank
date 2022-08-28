from django.urls import path
from .import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('details/<int:blog_id>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    
]
