# Generated by Django 3.0.4 on 2020-03-26 22:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zonas', '0003_auto_20200320_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]