# Generated by Django 3.1.4 on 2020-12-25 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracksapp', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracksapp',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tracksapp.category'),
            preserve_default=False,
        ),
    ]
