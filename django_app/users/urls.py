from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'

urlpatterns = [
    # Página de login
    path('login/', LoginView.as_view(template_name='users/login.html'), name= 'login'),
    # Página de Logout
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('base:index')), name='logout'),
]
