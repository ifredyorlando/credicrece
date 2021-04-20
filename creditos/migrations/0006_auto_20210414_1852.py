# Generated by Django 3.1.7 on 2021-04-15 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditos', '0005_auto_20210407_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='credito',
            name='cuota_capital',
            field=models.FloatField(default=0, verbose_name='Cuota capital'),
        ),
        migrations.AddField(
            model_name='credito',
            name='cuota_interes',
            field=models.FloatField(default=0, verbose_name='Cuota de interes'),
        ),
        migrations.AddField(
            model_name='credito',
            name='cuota_total_diaria',
            field=models.FloatField(default=0, verbose_name='Cuota total diaria'),
        ),
    ]
