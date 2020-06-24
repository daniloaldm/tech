from django.urls import path, include
from rest_framework import routers
from .views import (ProcessorView)

router = routers.DefaultRouter()
router.register(r'processors', ProcessorView)

urlpatterns = [
    path('api/', include(router.urls)),
]