# Generated by Django 3.2.8 on 2021-10-21 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clan', '0002_auto_20211021_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clan',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
