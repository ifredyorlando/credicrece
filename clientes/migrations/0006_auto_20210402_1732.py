# Generated by Django 3.1.7 on 2021-04-02 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20210401_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='apellido_de_casada',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Apellido de casada'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='primera_referencia_f',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre Primera Referencia Familiar'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='primera_referencia_p',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre de la Primera referencia'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='segunda_referencia_f',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre Segunda Referencia Familiar'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='segunda_referencia_p',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre de la Segunda referencia'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono_primera_referencia_f',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono de la Primera Referencia Familiar'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono_primera_referencia_p',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono de la Primera referencia'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono_segunda_referencia_f',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono de la Segunda Referencia Familiar'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono_segunda_referencia_p',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono de la Segunda referencia'),
        ),
    ]
