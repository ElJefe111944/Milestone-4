# Generated by Django 3.1.7 on 2021-03-01 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]