# Generated by Django 4.2.7 on 2023-11-27 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GYM', '0006_blog_alter_trainer_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='(gallery/')),
                ('title', models.CharField(max_length=50)),
                ('stock', models.IntegerField(default=0)),
                ('price', models.CharField(max_length=50)),
            ],
        ),
    ]
