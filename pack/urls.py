from rest_framework import routers
# from utilisateur.views import UtilisateurViewSet
from django.urls import path
from . import views
from pack.views import PackViewSet

routerPack = routers.DefaultRouter()
routerPack.register('',PackViewSet)

urlpatterns = [
    path('', views.list_pack),

]

# routerUtilisateur = routers.DefaultRouter()
# routerUtilisateur.register('',UtilisateurViewSet)