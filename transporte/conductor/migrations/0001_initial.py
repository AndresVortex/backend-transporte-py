# Generated by Django 4.2.1 on 2023-05-12 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.CharField(max_length=15, unique=True, verbose_name='identification')),
                ('nombre', models.CharField(max_length=20, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=20, null=True, verbose_name='apellido')),
                ('telefono', models.CharField(max_length=10, verbose_name='telefono')),
                ('direccion', models.CharField(max_length=50, null=True, verbose_name='direccion')),
            ],
        ),
    ]
