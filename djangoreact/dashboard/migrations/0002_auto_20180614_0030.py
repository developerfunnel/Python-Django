# Generated by Django 2.0.6 on 2018-06-14 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='business_point',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='list',
            field=models.ForeignKey(default=None, on_delete=True, related_name='cards', to='dashboard.List'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='story_point',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
