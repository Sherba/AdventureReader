# Generated by Django 3.0.6 on 2020-07-15 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_node_story'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='parent_node',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='stories.Node'),
        ),
        migrations.AlterField(
            model_name='node',
            name='child_nodes',
            field=models.ManyToManyField(related_name='children', to='stories.Node'),
        ),
    ]
