# Generated by Django 4.1.7 on 2023-03-25 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Timestamp',
            field=models.CharField(max_length=100),
        ),
    ]