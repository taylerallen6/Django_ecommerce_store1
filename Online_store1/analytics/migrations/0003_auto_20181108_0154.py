# Generated by Django 2.1.2 on 2018-11-08 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
        ('analytics', '0002_auto_20181108_0142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userds',
            name='user',
        ),
        migrations.AddField(
            model_name='userds',
            name='user_profile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_profile.UserProfile'),
        ),
    ]