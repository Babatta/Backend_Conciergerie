from rest_framework import routers
from django.urls import path,include
from . import views
from utilisateur.views import UtilisateurViewSet

routerUtilisateur = routers.DefaultRouter()
routerUtilisateur.register('utilisateur',UtilisateurViewSet)



urlpatterns = [
    path('', views.home),
    path(r'^utilisateur/$',views.utilisateurApi),
    path(r'^utilisateur/([0-9]+)$',views.utilisateurApi),




]

