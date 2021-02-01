# Generated by Django 3.1.5 on 2021-01-27 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rizin_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bantamplayer',
            name='age',
        ),
        migrations.RemoveField(
            model_name='bantamplayer',
            name='reach',
        ),
        migrations.RemoveField(
            model_name='featherplayer',
            name='age',
        ),
        migrations.RemoveField(
            model_name='featherplayer',
            name='reach',
        ),
        migrations.AddField(
            model_name='bantamplayer',
            name='birthday',
            field=models.CharField(max_length=20, null=True, verbose_name='生年月日'),
        ),
        migrations.AddField(
            model_name='featherplayer',
            name='birthday',
            field=models.CharField(max_length=20, null=True, verbose_name='生年月日'),
        ),
    ]