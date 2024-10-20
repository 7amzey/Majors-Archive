# Generated by Django 4.2 on 2023-07-07 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('majorsweb', '0017_alter_team_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=500)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='videos', to='majorsweb.subject')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='majorsweb.team')),
            ],
        ),
    ]