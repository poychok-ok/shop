# Generated by Django 5.1.1 on 2024-10-05 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=20)),
                ('quantity', models.PositiveIntegerField()),
                ('descrition', models.TextField()),
                ('img', models.ImageField(upload_to='images/')),
                ('discounts', models.PositiveIntegerField(default=0)),
                ('ratind', models.FloatField(verbose_name=0)),
                ('is_avalable', models.BooleanField(verbose_name=True)),
            ],
        ),
    ]
