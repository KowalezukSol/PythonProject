# Generated by Django 5.0.2 on 2024-03-08 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mi_app', '0002_cliente_usuario_envio_usuario_producto_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='envio',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Envio',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
