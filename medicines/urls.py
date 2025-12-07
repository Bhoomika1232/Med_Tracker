from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'medicines'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='medicines/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', views.dashboard, name='dashboard'),                # requires login
    path('medicine/add/', views.medicine_create, name='medicine_add'),
    path('medicine/<int:pk>/edit/', views.medicine_update, name='medicine_edit'),
    path('medicine/<int:pk>/delete/', views.medicine_delete, name='medicine_delete'),
]