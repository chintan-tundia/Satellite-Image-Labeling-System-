# Generated by Django 2.2.1 on 2019-09-02 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gmapv2', '0009_auto_20190827_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='gmapmarker',
            name='ground_truthing_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='jsmappedworks',
            name='is_marked',
            field=models.BooleanField(default=False),
        ),
    ]