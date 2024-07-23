from django.urls import path

from . import views

app_name = 'usuarios'

urlpatterns = [
    path('cadastro/', views.cadastro_view, name="cadastro"),
    path('cadastro/create/', views.cadastro_create, name="create"),
    path('login/', views.login_view, name="login"),
    path('login/create/', views.login_create, name="login_create"),
    path('logout/', views.logout_view, name="logout"),
    path('emprestimos/', views.emprestimos, name="emprestimos"),
]