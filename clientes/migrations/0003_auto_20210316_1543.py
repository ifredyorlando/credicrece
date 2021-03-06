# Generated by Django 3.1.7 on 2021-03-16 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20210316_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='condicion_vivienda',
            field=models.CharField(choices=[('propia', 'Propia'), ('alquilada', 'Alquilada'), ('usufructo', 'Usufructo'), ('familiar', 'Familiar'), ('adeudada', 'Adeuda'), ('prestada', 'Prestada')], default='propia', max_length=25, verbose_name='Condicion de vivienda'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='estado_civil',
            field=models.CharField(choices=[('soltero', 'Soltero'), ('casado', 'Casado')], default='soltero', max_length=25, verbose_name='Estado Civil'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='primera_referencia_f',
            field=models.CharField(max_length=50, verbose_name='Nombre Primera Referencia Familiar'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='primera_referencia_p',
            field=models.CharField(max_length=50, verbose_name='Nombre de la Primera referencia'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='segunda_referencia_f',
            field=models.CharField(max_length=50, verbose_name='Nombre Segunda Referencia Familiar'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='segunda_referencia_p',
            field=models.CharField(max_length=50, verbose_name='Nombre de la Segunda referencia'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono_primera_referencia_f',
            field=models.CharField(max_length=50, verbose_name='Telefono de la Primera Referencia Familiar'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono_primera_referencia_p',
            field=models.CharField(max_length=50, verbose_name='Telefono de la Primera referencia'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono_segunda_referencia_f',
            field=models.CharField(max_length=50, verbose_name='Telefono de la Segunda Referencia Familiar'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono_segunda_referencia_p',
            field=models.CharField(max_length=50, verbose_name='Telefono de la Segunda referencia'),
        ),
    ]
