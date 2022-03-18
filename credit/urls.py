from rest_framework import routers
# from utilisateur.views import UtilisateurViewSet
from django.urls import path
from . import views
from credit.views import CreditViewSet

routerCredit = routers.DefaultRouter()
routerCredit.register('',CreditViewSet)

urlpatterns = [
    path('', views.list_credit),

]

# routerUtilisateur = routers.DefaultRouter()
# routerUtilisateur.register('',UtilisateurViewSet)