# Generated by Django 3.0.8 on 2020-07-27 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assy', '0002_message_request_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='roommodel',
            name='request_user',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
