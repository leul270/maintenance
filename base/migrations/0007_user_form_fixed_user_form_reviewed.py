# Generated by Django 5.0.1 on 2024-02-04 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_technician_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_form',
            name='fixed',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='user_form',
            name='reviewed',
            field=models.BooleanField(default=False, null=True),
        ),
    ]