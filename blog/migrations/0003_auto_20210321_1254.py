# Generated by Django 3.1.7 on 2021-03-21 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210320_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='blog_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(max_length=55),
        ),
    ]
