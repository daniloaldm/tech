from django.urls import path, include
from rest_framework import routers
from .views import (ProcessorView, VideoCardView)

router = routers.DefaultRouter()
router.register(r'processors', ProcessorView)
router.register(r'videocards', VideoCardView)

urlpatterns = [
    path('api/', include(router.urls)),
]