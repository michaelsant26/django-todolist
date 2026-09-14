from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . forms import BootstrapLoginForm

urlpatterns = [
    path('', views.task_list, name = 'task_list'),
    path('add/', views.add_task, name = 'add_task'),
    path('toggle/<int:task_id>/', views.toggle_status, name = 'toggle_status'),
    path('edit/<int:task_id>/', views.edit_task, name = 'edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name = 'delete_task'),
    path('register/', views.register, name = 'register'),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='todo/login.html',
            authentication_form=BootstrapLoginForm
        ),
        name='login'
    ),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
