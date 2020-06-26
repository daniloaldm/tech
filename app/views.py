from rest_framework import viewsets, filters, generics
from .models import (Processor, VideoCard, RamMemory, Motherboard)
from .serializers import *

class ProcessorView(viewsets.ReadOnlyModelViewSet):
    queryset = Processor.objects.all()
    serializer_class = ProcessorSerializer
    filter_fields = "__all__"

class VideoCardView(viewsets.ReadOnlyModelViewSet):
    queryset = VideoCard.objects.all()
    serializer_class = VideoCardSerializer
    filter_fields = "__all__"

class RamMemoryView(viewsets.ReadOnlyModelViewSet):
    queryset = RamMemory.objects.all()
    serializer_class = RamMemorySerializer
    filter_fields = "__all__"

class MotherboardView(viewsets.ReadOnlyModelViewSet):
    queryset = Motherboard.objects.all()
    serializer_class = MotherboardSerializer
    filter_fields = "__all__"