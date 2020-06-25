# Generated by Django 3.0.7 on 2020-06-25 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Processor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processor', models.CharField(choices=[('Intel Core i5', 'Intel Core i5'), ('Intel Core i7', 'Intel Core i7'), ('AMD Athlon', 'AMD Athlon'), ('AMD Ryzen 7', 'AMD Ryzen 7')], max_length=100)),
                ('processor_brand', models.CharField(choices=[('Intel', 'Intel'), ('AMD', 'AMD')], max_length=100)),
            ],
        ),
    ]