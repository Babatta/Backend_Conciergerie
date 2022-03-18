from rest_framework import routers
from django.urls import path
from . import views
from boite.views import BoiteViewSet

routerBoite = routers.DefaultRouter()
routerBoite.register('',BoiteViewSet)

urlpatterns = [
    path('', views.list_boite),

]

# routerUtilisateur = routers.DefaultRouter()
# routerUtilisateur.register('',UtilisateurViewSet)