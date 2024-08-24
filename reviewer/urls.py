from django.urls import path
from . import views

urlpatterns = [
    path('reviewer/', views.reviewer, name='reviewer'),
]