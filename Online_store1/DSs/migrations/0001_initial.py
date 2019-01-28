# Generated by Django 2.1.2 on 2018-11-08 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_profile', '0002_remove_userprofile_products'),
        ('products', '0003_product_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('male', models.DecimalField(decimal_places=5, default=0.0, max_digits=15)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='UserDS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('male', models.DecimalField(decimal_places=5, default=0.0, max_digits=15)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user_profile', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_profile.UserProfile')),
            ],
        ),
    ]
