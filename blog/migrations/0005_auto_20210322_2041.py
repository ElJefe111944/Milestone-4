# Generated by Django 3.1.7 on 2021-03-22 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210321_1400'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='post',
            name='info',
            field=models.CharField(default='Summary', max_length=55),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=55),
        ),
    ]