# Generated by Django 4.2 on 2024-05-31 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('majorsweb', '0026_rename_union_logo_dark_team_union_dark_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects_category',
            name='hours',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]