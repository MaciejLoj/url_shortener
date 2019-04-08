# Generated by Django 2.2 on 2019-04-06 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortenerapp', '0003_auto_20190406_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlshortener',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='urlshortener',
            name='short_url',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]