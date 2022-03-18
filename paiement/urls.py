from rest_framework import routers
# from utilisateur.views import UtilisateurViewSet
from django.urls import path
from . import views
from paiement.views import PaiementViewSet

routerPaiement = routers.DefaultRouter()
routerPaiement.register('',PaiementViewSet)

urlpatterns = [
    path('', views.list_paiement),

]

# routerUtilisateur = routers.DefaultRouter()
# routerUtilisateur.register('',UtilisateurViewSet)