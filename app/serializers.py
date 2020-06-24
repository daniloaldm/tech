from rest_framework import serializers
from .models import (Processor)


class ProcessorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Processor
        fields = '__all__'
