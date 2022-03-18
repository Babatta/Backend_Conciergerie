from rest_framework import routers
from django.urls import path
from . import views
from localisation.views import LocalisationViewSet

routerLocalisation = routers.DefaultRouter()
routerLocalisation.register('',LocalisationViewSet)

urlpatterns = [
    path('', views.localisation),
]
