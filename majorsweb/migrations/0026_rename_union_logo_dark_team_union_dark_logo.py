# Generated by Django 4.2 on 2024-05-14 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('majorsweb', '0025_remove_team_union_logo_team_union_light_logo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='union_logo_dark',
            new_name='union_dark_logo',
        ),
    ]