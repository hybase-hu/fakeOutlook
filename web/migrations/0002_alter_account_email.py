# Generated by Django 4.0.1 on 2023-02-10 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
