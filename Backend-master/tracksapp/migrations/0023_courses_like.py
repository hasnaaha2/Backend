# Generated by Django 3.1.7 on 2021-02-22 11:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracksapp', '0022_auto_20210215_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='like',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
