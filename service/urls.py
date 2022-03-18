from rest_framework import routers
# from utilisateur.views import UtilisateurViewSet
from django.urls import path
from . import views
from service.views import ServiceViewSet

routerService = routers.DefaultRouter()
routerService.register('',ServiceViewSet)

urlpatterns = [
    path('', views.list_service),

]

# routerUtilisateur = routers.DefaultRouter()
# routerUtilisateur.register('',UtilisateurViewSet)