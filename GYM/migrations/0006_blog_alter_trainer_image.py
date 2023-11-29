# Generated by Django 4.2.7 on 2023-11-27 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GYM', '0005_trainer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tab_name', models.CharField(choices=[('events and competitions', 'nutrition tips'), ('body building', 'pilates and yoga'), ('workout', 'fitness'), ('wellness treatments', 'uncategorized')], max_length=50)),
                ('blogimage', models.ImageField(upload_to='blogs/')),
                ('about', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='trainer',
            name='image',
            field=models.ImageField(upload_to='my-trainers/'),
        ),
    ]
