from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [path('', views.home_view),
               path('skill/', views.skill_view),
               path('work/', views.work_view),
               path('comment/', views.comment_view),
               path('comment/save/', views.comment_create),
               ]