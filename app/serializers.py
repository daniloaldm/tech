from rest_framework import serializers
from .models import (Processor, VideoCard, RamMemory, Motherboard, Computer, Order)


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

class MotherboardSerializer(serializers.ModelSerializer):

    class Meta:

        model = Motherboard
        fields = '__all__'

class ComputerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Computer
        fields = "__all__"

    # def validate(self, data):
    #     Validators.number_ram(data)
    #     Validators.ram_size(data)
    #     Validators.processor(data)
    #     Validators.video_board(data)
    #     return data

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"