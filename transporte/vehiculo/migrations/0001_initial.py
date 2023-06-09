# Generated by Django 4.2.1 on 2023-05-12 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('conductor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=8, verbose_name='modelo')),
                ('placa', models.CharField(max_length=7, unique=True, verbose_name='placa')),
                ('capacidad', models.CharField(max_length=7, null=True, verbose_name='capacidad')),
                ('conductor_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conductor_id', to='conductor.driver')),
            ],
        ),
    ]
