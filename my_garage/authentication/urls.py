from django.urls import path

from .views import AuthView, AuthLogoutView

AUTH_PATH = 'auth'
app_name = AUTH_PATH


urlpatterns = [
    path(AUTH_PATH, AuthView.as_view()),
    path(f'{AUTH_PATH}/logout', AuthLogoutView.as_view()),
]
