from django.contrib import admin
from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('blog/<str:pk>/', views.blog, name="blog"),
    path('blog_update/<str:pk>/',
         views.BlogUpdate.as_view(), name='blogupdate'),
    path('blogadd/', views.BlogCreate.as_view(), name='blogadd'),
    path('category_create/', views.CategoryCreate.as_view(), name='categoryadd'),
]
