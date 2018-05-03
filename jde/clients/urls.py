from django.conf.urls import url
from clients.views import ClientList

urlpatterns = [
    url(r'^$', ClientList.as_view(), name='clients_list'),
]