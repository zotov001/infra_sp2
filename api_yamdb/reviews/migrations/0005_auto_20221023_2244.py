# Generated by Django 2.2.16 on 2022-10-23 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20221022_1519'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('title', 'author')},
        ),
    ]