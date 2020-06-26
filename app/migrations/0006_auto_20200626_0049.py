# Generated by Django 3.0.7 on 2020-06-26 00:49

from django.db import migrations


def populate_rammemorys(apps, schema_editor):

    RamMemory = apps.get_model('app', 'rammemory')
    [
        RamMemory(ram_memory="Hiper X", ram_memory_size=4).save(),
        RamMemory(ram_memory="Hiper X", ram_memory_size=8).save(),
        RamMemory(ram_memory="Hiper X", ram_memory_size=16).save(),
        RamMemory(ram_memory="Hiper X", ram_memory_size=32).save(),
        RamMemory(ram_memory="Hiper X", ram_memory_size=64).save(),
    ]


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rammemory'),
    ]

    operations = [
        migrations.RunPython(populate_rammemorys)
    ]