# Generated by Django 2.1.3 on 2018-11-14 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiries', '0003_auto_20181114_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='user',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]