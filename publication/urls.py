from rest_framework import routers
# from utilisateur.views import UtilisateurViewSet
from django.urls import path
from . import views
from publication.views import PublicationViewSet

routerPublication = routers.DefaultRouter()
routerPublication.register('',PublicationViewSet)

urlpatterns = [
    path('', views.list_publication),

]

# routerUtilisateur = routers.DefaultRouter()
# routerUtilisateur.register('',UtilisateurViewSet)