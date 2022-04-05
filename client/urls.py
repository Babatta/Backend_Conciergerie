from rest_framework import routers
# from utilisateur.views import UtilisateurViewSet
from django.urls import path
from . import views
from client.views import ClientViewSet

routerClient = routers.DefaultRouter()
routerClient.register('',ClientViewSet)


urlpatterns = [
    path('', views.list_client),
    path(r'^client/$', views.clientApi),
    path(r'^client/([0-9]+)$', views.clientApi),

]

# routerUtilisateur = routers.DefaultRouter()
# routerUtilisateur.register('',UtilisateurViewSet)