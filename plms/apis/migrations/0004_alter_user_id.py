# Generated by Django 3.2.7 on 2021-10-31 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_auto_20211031_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
