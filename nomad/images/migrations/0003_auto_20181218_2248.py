# Generated by Django 2.0.9 on 2018-12-18 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20181218_2029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='message',
            new_name='creator',
        ),
    ]
