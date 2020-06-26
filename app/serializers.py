from rest_framework import serializers
from .models import (Processor, VideoCard)


class ProcessorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Processor
        fields = '__all__'

class VideoCardSerializer(serializers.ModelSerializer):

    class Meta:

        model = VideoCard
        fields = '__all__'
