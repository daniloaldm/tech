from rest_framework import viewsets, filters, generics
from .models import (Processor)
from .serializers import *

class ProcessorView(viewsets.ReadOnlyModelViewSet):
    queryset = Processor.objects.all()
    serializer_class = ProcessorSerializer
    filter_fields = "__all__"