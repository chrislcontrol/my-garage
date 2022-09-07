from django.urls import path

from .views import ClientsView

CLIENTS_PATH = 'clients'
app_name = CLIENTS_PATH


urlpatterns = [
    path(CLIENTS_PATH, ClientsView.as_view(), name=f'{CLIENTS_PATH}-create'),
]
