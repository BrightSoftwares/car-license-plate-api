from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('owners', views.OwnerView)
router.register('plates', views.PlateView)

urlpatterns = [
    path('', include(router.urls), name='index'),
    path('owners/', views.OwnerView, name='owners'),
    path('plates/', views.OwnerView, name='plates'),
]
