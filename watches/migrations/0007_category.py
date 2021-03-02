# Generated by Django 3.1.7 on 2021-03-02 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watches', '0006_auto_20210302_0827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
