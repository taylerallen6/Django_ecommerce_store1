# Generated by Django 2.1.2 on 2018-11-03 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20181102_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.TextField(blank=True, null=True),
        ),
    ]
