# Generated by Django 3.1.7 on 2021-04-15 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditos', '0006_auto_20210414_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credito',
            name='cuota_total_diaria',
        ),
        migrations.AddField(
            model_name='credito',
            name='cuota_total',
            field=models.FloatField(default=0, verbose_name='Cuota total'),
        ),
        migrations.AddField(
            model_name='credito',
            name='cuotas_pendientes',
            field=models.FloatField(default=0, verbose_name='Cantidad de cuotas pendientes'),
        ),
    ]