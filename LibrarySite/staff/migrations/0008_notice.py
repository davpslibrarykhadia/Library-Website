# Generated by Django 4.1.7 on 2023-04-22 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0007_contactdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('Sno', models.AutoField(primary_key=True, serialize=False)),
                ('notice', models.TextField()),
            ],
        ),
    ]
