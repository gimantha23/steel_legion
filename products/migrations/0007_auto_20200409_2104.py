# Generated by Django 3.0.5 on 2020-04-09 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200409_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('ASSAULT', 'Assault'), ('SNIPER', 'Sniper'), ('SMG', 'SMG'), ('LMG', 'LMG'), ('SHOTGUN', 'Shot gun'), ('HANDGUN', 'Hand gun')], max_length=15),
        ),
    ]