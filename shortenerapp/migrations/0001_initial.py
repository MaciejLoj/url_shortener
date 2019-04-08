# Generated by Django 2.2 on 2019-04-08 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URLShortener',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=300)),
                ('short_url', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
