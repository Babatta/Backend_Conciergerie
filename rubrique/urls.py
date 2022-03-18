from rest_framework import routers
# from utilisateur.views import UtilisateurViewSet
from django.urls import path
from . import views
from rubrique.views import CreditViewSet

routerRubrique = routers.DefaultRouter()
routerRubrique.register('',CreditViewSet)

urlpatterns = [
    path('', views.list_rubrique),

]

# routerUtilisateur = routers.DefaultRouter()
# routerUtilisateur.register('',UtilisateurViewSet)