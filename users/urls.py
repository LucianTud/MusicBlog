from django.urls import path
from . import views  # Asigură-te că folosești `views` din aplicația `users`

app_name = 'users'  # Setează namespace-ul corect

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    # alte URL-uri pentru aplicația users
]

