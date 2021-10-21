# Generated by Django 3.2.8 on 2021-10-21 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clan', '0001_initial'),
        ('Player', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='clan_leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leader', to='Clan.clan'),
        ),
    ]
