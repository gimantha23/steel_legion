# Generated by Django 3.0.5 on 2020-04-07 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('type', models.CharField(choices=[('ASSAULT', 'Assault'), ('SNIPER', 'Sniper'), ('SMG', 'SMG'), ('LMG', 'LMG'), ('SHOTGUN', 'Shot gun')], max_length=15)),
                ('image', models.FileField(upload_to='products/')),
                ('description', models.TextField(max_length=500)),
            ],
        ),
    ]
