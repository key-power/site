# Generated by Django 4.0.6 on 2023-01-17 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homme', '0013_alter_price_icon_alter_service_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='content',
            field=models.TextField(max_length=200),
        ),
    ]
