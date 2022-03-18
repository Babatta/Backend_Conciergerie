from rest_framework import routers
from abonne.views import AbonneViewSet
from django.urls import path
from . import views
routerAbonne = routers.DefaultRouter()
routerAbonne.register('',AbonneViewSet)

urlpatterns = [
    path('', views.list_abonne),

]

