# Generated by Django 4.0.1 on 2023-02-23 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('random_numbers_app', '0002_lottery_results_delete_oregon_results'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='lottery_results',
            new_name='LotteryResults',
        ),
    ]
