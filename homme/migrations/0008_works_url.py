# Generated by Django 4.0.6 on 2022-07-11 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homme', '0007_works_photo_alter_partners_photo_alter_team_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='works',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]