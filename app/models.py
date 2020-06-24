# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations, models
from django.utils import timezone


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
