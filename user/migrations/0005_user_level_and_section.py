# Generated by Django 3.2 on 2021-10-06 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_levelandsection'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='level_and_section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_level_and_section', to='user.levelandsection'),
        ),
    ]
