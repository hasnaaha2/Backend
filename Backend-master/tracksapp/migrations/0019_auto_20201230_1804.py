# Generated by Django 3.1.4 on 2020-12-30 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracksapp', '0018_auto_20201230_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='thirdcourse_title',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
