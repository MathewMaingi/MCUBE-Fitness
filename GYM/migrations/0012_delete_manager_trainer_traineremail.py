# Generated by Django 4.2.7 on 2023-11-28 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GYM', '0011_manager_trainer_trainerpassword_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Manager',
        ),
        migrations.AddField(
            model_name='trainer',
            name='traineremail',
            field=models.EmailField(default='@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]
