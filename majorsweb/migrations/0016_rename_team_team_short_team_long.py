# Generated by Django 4.2 on 2023-05-21 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('majorsweb', '0015_team_union_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='team',
            new_name='short',
        ),
        migrations.AddField(
            model_name='team',
            name='long',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]