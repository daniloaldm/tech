from django.urls import path, include
from rest_framework import routers
from .views import (ProcessorView, VideoCardView, RamMemoryView, MotherboardView)

router = routers.DefaultRouter()
router.register(r'processors', ProcessorView)
router.register(r'videocards', VideoCardView)
router.register(r'rammemorys', RamMemoryView)
router.register(r'motherboards', MotherboardView)

urlpatterns = [
    path('api/', include(router.urls)),
]