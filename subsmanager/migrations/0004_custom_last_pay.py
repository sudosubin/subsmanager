# Generated by Django 2.1.8 on 2019-06-29 15:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('subsmanager', '0003_remove_custom_lastpay'),
    ]

    operations = [
        migrations.AddField(
            model_name='custom',
            name='last_pay',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
