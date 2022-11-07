# Generated by Django 4.1.1 on 2022-10-19 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('releasedate', models.DateField()),
                ('moviename', models.CharField(max_length=30)),
                ('actor', models.CharField(max_length=30)),
                ('actress', models.CharField(max_length=30)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
