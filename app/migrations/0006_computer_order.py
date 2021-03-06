# Generated by Django 3.0.7 on 2020-07-16 02:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_auto_20200626_0237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memory_id', models.ManyToManyField(to='app.RamMemory')),
                ('mother_board_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Motherboard')),
                ('processor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Processor')),
                ('video_board_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.VideoCard')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computer_id', models.ManyToManyField(to='app.Computer')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
