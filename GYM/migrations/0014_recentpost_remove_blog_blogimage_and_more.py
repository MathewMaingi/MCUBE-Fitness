# Generated by Django 4.2.7 on 2023-11-29 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GYM', '0013_remove_trainer_traineremail'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecentPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('about', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='blogimage',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='tab_name',
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='default', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='about',
            field=models.CharField(default='about', max_length=100),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(default='describe'),
        ),
    ]
