from rest_framework import routers
from django.urls import path
from . import views
from utilisateur.views import UtilisateurViewSet

routerUtilisateur = routers.DefaultRouter()
routerUtilisateur.register('utilisateur',UtilisateurViewSet)

urlpatterns = [
    path('', views.home),
]

