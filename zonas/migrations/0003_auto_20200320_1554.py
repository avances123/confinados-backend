# Generated by Django 3.0.4 on 2020-03-20 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zonas', '0002_mensaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='zona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes', to='zonas.Zona'),
        ),
    ]
