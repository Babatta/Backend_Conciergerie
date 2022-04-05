from rest_framework import routers
# from utilisateur.views import UtilisateurViewSet
from django.urls import path
from . import views
from administrateur.views import AdministrateurViewSet

routerAdministrateur = routers.DefaultRouter()
routerAdministrateur.register('',AdministrateurViewSet)

urlpatterns = [
    path('', views.list_administrateur),
    path(r'^administrateur/$', views.administrateurApi),
    path(r'^administrateur/([0-9]+)$', views.administrateurApi),

]

# routerUtilisateur = routers.DefaultRouter()
# routerUtilisateur.register('',UtilisateurViewSet)