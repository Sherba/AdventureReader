# Generated by Django 3.0.8 on 2020-07-20 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0009_post_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='genres',
            field=models.ManyToManyField(null=True, to='stories.Genre'),
        ),
    ]
