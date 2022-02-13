# Generated by Django 4.0 on 2022-02-13 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charactermodel',
            name='category',
            field=models.CharField(choices=[('1', '64'), ('2', 'melee'), ('3', 'brawl'), ('4', 'for'), ('5', 'ultimate')], max_length=10),
        ),
        migrations.AlterField(
            model_name='charactermodel',
            name='type',
            field=models.CharField(choices=[('0', 'super-heavy'), ('1', 'heavy'), ('2', 'heavy-middle'), ('3', 'middle'), ('4', 'middle-light'), ('5', 'light'), ('6', 'super-light')], max_length=15),
        ),
    ]
