
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('run_update/<int:id>/', views.run_update, name='run_update'),
    path('signup', views.register, name='register')
]