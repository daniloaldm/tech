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
    

    def create(self, validated_data):

        # validator number_ram
        num_slots = validated_data['mother_board_id'].r_slots
        num_ram = len(validated_data['memory_id'])

        if num_slots < num_ram:
            raise (
                serializers.ValidationError(
                    f"Número de ram selecionada maior do que a suportada pela placa mãe. Suportada: {num_slots} Pedida: {num_ram}")
            )
        
        # validator ram_size
        ram_size_request = sum(
            [memory.ram_memory_size for memory in validated_data['memory_id']])

        ram_size_suported = validated_data['mother_board_id'].m_ram

        if ram_size_request > ram_size_suported:
            raise (
                serializers.ValidationError(
                    f"A placa mãe selecioanada não suporta essa quantidade de Ram pedida. Suportada: {ram_size_suported} Pedida: {ram_size_request}"
                )
            )

        # validator processor
        supported_brand = validated_data['mother_board_id'].supp_processors
        requested_brand = validated_data['processor_id'].processor_brand

        if(supported_brand != 'Intel e AMD' and supported_brand != requested_brand):
            raise (
                serializers.ValidationError(
                    f"A Placa mãe selecionada não suporta essa marca de processador. Suportada: {supported_brand} Pedida: {requested_brand}"
                )
            )
        
        # validator video_board
        has_video_integrated = validated_data['mother_board_id'].has_integrated_video

        if( not has_video_integrated and not validated_data['video_board_id']):
            raise (
                serializers.ValidationError(
                    "A Placa mãe selecionada requer uma placa de vídeo"
                )
            )

        return validated_data
    
class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"