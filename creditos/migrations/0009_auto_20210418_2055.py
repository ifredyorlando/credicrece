# Generated by Django 3.1.7 on 2021-04-19 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditos', '0008_credito_cuota_total_diaria'),
    ]

    operations = [
        migrations.AddField(
            model_name='credito',
            name='desembolsado',
            field=models.BooleanField(default=False, verbose_name='Credito desembolsado'),
        ),
        migrations.AddField(
            model_name='credito',
            name='pagado',
            field=models.BooleanField(default=False, verbose_name='Credito pagado'),
        ),
    ]
