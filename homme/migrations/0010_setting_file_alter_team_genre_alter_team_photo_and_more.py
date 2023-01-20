# Generated by Django 4.0.6 on 2023-01-16 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homme', '0009_partner_work_rename_reviews_review_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='file',
            field=models.FileField(blank=True, upload_to='setting/'),
        ),
        migrations.AlterField(
            model_name='team',
            name='genre',
            field=models.CharField(choices=[('MAN', 'Man'), ('WOMAN', 'Woman')], max_length=10),
        ),
        migrations.AlterField(
            model_name='team',
            name='photo',
            field=models.ImageField(blank=True, upload_to='teams/'),
        ),
        migrations.AlterField(
            model_name='work',
            name='photo',
            field=models.ImageField(blank=True, upload_to='works/'),
        ),
    ]