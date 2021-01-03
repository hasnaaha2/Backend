# Generated by Django 3.1.4 on 2020-12-29 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracksapp', '0012_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=400)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracksapp.tracksapp')),
            ],
        ),
        migrations.DeleteModel(
            name='course',
        ),
    ]