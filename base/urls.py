from django.contrib import admin
from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('blog/<str:pk>/', views.blog, name="blog"),
    path('blog_update/<str:pk>/',
         views.BlogUpdate.as_view(), name="blogupdate"),
    path('blog_create/', views.BlogCreate.as_view(), name="blogadd"),
]
