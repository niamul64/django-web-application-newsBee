# Generated by Django 2.2 on 2021-01-03 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_share_newsauthor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='share',
            old_name='newDate',
            new_name='newsDate',
        ),
    ]