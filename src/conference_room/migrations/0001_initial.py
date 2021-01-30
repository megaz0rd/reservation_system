# Generated by Django 2.2.17 on 2021-01-30 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConferenceRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('capacity', models.PositiveSmallIntegerField()),
                ('projector', models.BooleanField(default=False)),
            ],
        ),
    ]