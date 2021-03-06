from django.urls import path, include
from rest_framework import routers
from .views import (ProcessorView, VideoCardView, RamMemoryView, MotherboardView, ComputerView, OrderView)

router = routers.DefaultRouter()
router.register(r'processors', ProcessorView)
router.register(r'videocards', VideoCardView)
router.register(r'rammemorys', RamMemoryView)
router.register(r'motherboards', MotherboardView)
router.register(r'computers', ComputerView)
router.register(r'orders', OrderView)

urlpatterns = [
    path('', include(router.urls)),
]