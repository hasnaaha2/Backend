# Generated by Django 3.1.4 on 2020-12-26 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracksapp', '0007_auto_20201226_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracksapp',
            name='trackpathname',
        ),
    ]