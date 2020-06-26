from rest_framework import serializers
from .models import (Processor, VideoCard, RamMemory)


class ProcessorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Processor
        fields = '__all__'

class VideoCardSerializer(serializers.ModelSerializer):

    class Meta:

        model = VideoCard
        fields = '__all__'


class RamMemorySerializer(serializers.ModelSerializer):

    class Meta:

        model = RamMemory
        fields = '__all__'