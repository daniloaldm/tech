# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models
from django.utils import timezone
from django.contrib.auth.models import User


class Processor(models.Model):
    available_processors = [
        ("Intel Core i5", "Intel Core i5"),
        ("Intel Core i7", "Intel Core i7"),
        ("AMD Athlon", "AMD Athlon"),
        ("AMD Ryzen 7", "AMD Ryzen 7")]
        
    brand_of_processors = [
        ("Intel", "Intel"),
        ("AMD", "AMD")]

    processor = models.CharField(max_length=100, choices=available_processors)
    processor_brand = models.CharField(max_length=100, choices=brand_of_processors)

    def __str__(self):
        return f"{self.processor}"

class VideoCard(models.Model):
    available_videocards = [
        ("Gigabyte Geforce GTX 1060 6GB", "Gigabyte Geforce GTX 1060 6GB"),
        ("PNY RTX 2060 6GB", "PNY RTX 2060 6GB"),
        ("Radeon RX 580 8GB", "Radeon RX 580 8GB"),
    ]

    video_card= models.CharField(max_length=100, choices=available_videocards)

    def __str__(self):
        return f"{self.video_card}"

class RamMemory(models.Model):
    available_ram = [
        ("Hiper X", "Hiper X"),
    ]
        
    ram_size = [
        (4, "4"), (8, "8"),
        (16, "16"), (32, "32"), (64, "64")
    ]

    ram_memory = models.CharField(max_length=100, choices=available_ram)
    ram_memory_size = models.PositiveIntegerField(choices=ram_size)

    def __str__(self):
        return f"{self.ram_memory} {self.ram_memory_size}GB"

class Motherboard(models.Model):
    available_motherboard = [
        ("Asus Prime", "Asus Prime"),
        ("Gigabyte", "Gigabyte"),
        ("ASRock Fatal", "ASRock Fatal")
    ]

    supported_processors = [
        ("Intel", "Intel"),
        ("AMD", "AMD"),
        ("Intel e AMD", "Intel e AMD")
    ]
        
    ram_slots = [
        (2, "2"),
        (4, "4")
    ]

    max_ram = [
        (16, "16"),
        (64, "64")
    ]

    motherboard = models.CharField(max_length=100, choices=available_motherboard)
    supp_processors = models.CharField(max_length=100, choices=supported_processors)
    r_slots = models.PositiveIntegerField(choices=ram_slots)
    m_ram = models.PositiveIntegerField(choices=max_ram)
    has_integrated_video = models.BooleanField()

    def __str__(self):
        return f"{self.motherboard}"

class Computer(models.Model):
    mother_board_id = models.ForeignKey(Motherboard, on_delete=models.CASCADE)
    video_board_id = models.ForeignKey(VideoCard, on_delete=models.CASCADE, blank=False, null=True)
    processor_id = models.ForeignKey(Processor, on_delete=models.CASCADE)
    memory_id = models.ManyToManyField(RamMemory)

    def sum_ram(self):

        memories = list(self.memory_id.values())
        total_size = 0

        for memory in memories:
            total_size += memory['ram_memory_size']
        return total_size

    def __str__(self):
        base_string = f"{self.mother_board_id} {self.processor_id} {self.sum_ram()} GB "

        if self.video_board_id is None:
            return base_string
        return f"{base_string} {self.video_board_id.video_card}"

class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    computer_id = models.ManyToManyField(Computer)

    def __str__(self):
        return f"Usuário {self.user_id.username} fez o pedido do computador: {self.computador_id}"