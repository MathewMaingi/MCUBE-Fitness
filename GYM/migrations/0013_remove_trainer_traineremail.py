# Generated by Django 4.2.7 on 2023-11-28 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GYM', '0012_delete_manager_trainer_traineremail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='traineremail',
        ),
    ]
