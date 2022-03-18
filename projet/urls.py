"""projet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from utilisateur.urls import routerUtilisateur as utilisateur_router
from localisation.urls import routerLocalisation as localisation_router
from abonne.urls import routerAbonne as abonne_router
from administrateur.urls import routerAdministrateur as administrateur_router
from boite.urls import routerBoite as boite_router
from client.urls import routerClient as client_router
from credit.urls import routerCredit as credit_router
from pack.urls import routerPack as pack_router
from paiement.urls import routerPaiement as paiement_router
from publication.urls import routerPublication as publication_router
from rubrique.urls import routerRubrique as rubrique_router
from service.urls import routerService as service_router



routerUtilisateur = routers.DefaultRouter()
routerUtilisateur.registry.extend(utilisateur_router.registry)

routerLocalisation = routers.DefaultRouter()
routerLocalisation.registry.extend(localisation_router.registry)

routerAbonne = routers.DefaultRouter()
routerAbonne.registry.extend(abonne_router.registry)

routerAdministrateur = routers.DefaultRouter()
routerAdministrateur.registry.extend(administrateur_router.registry)

routerBoite = routers.DefaultRouter()
routerBoite.registry.extend(boite_router.registry)

routerClient = routers.DefaultRouter()
routerClient.registry.extend(client_router.registry)

routerCredit = routers.DefaultRouter()
routerCredit.registry.extend(credit_router.registry)

routerPack = routers.DefaultRouter()
routerPack.registry.extend(pack_router.registry)

routerPaiement = routers.DefaultRouter()
routerPaiement.registry.extend(paiement_router.registry)

routerPubication = routers.DefaultRouter()
routerPubication.registry.extend(publication_router.registry)

routerRubrique = routers.DefaultRouter()
routerRubrique.registry.extend(rubrique_router.registry)

routerService = routers.DefaultRouter()
routerService.registry.extend(service_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(routerUtilisateur.urls)),
    path('abonne', include(routerAbonne.urls)),
    path('administrateur', include(routerAdministrateur.urls)),
    path('boite', include(routerBoite.urls)),
    path('client', include(routerClient.urls)),
    path('credit', include(routerCredit.urls)),
    path('localisation', include(routerLocalisation.urls)),
    path('pack', include(routerPack.urls)),
    path('paiement', include(routerPaiement.urls)),
    path('publication', include(routerPubication.urls)),
    path('rubrique', include(routerRubrique.urls)),
    path('service', include(routerService.urls)),

]
