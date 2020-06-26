from django.urls import path, include
from rest_framework import routers
from .views import (ProcessorView, VideoCardView, RamMemoryView)

router = routers.DefaultRouter()
router.register(r'processors', ProcessorView)
router.register(r'videocards', VideoCardView)
router.register(r'rammemorys', RamMemoryView)

urlpatterns = [
    path('api/', include(router.urls)),
]