# Generated by Django 3.0.4 on 2020-03-26 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zonas', '0004_mensaje_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='autor',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mensaje',
            name='titulo',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
