# Generated by Django 4.0.4 on 2022-06-01 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('artist_name', models.CharField(max_length=20)),
                ('art_fields', models.TextField()),
                ('country', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=40)),
                ('project_type', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('add_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_piece', models.CharField(max_length=40)),
                ('art_type', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('available', models.BooleanField()),
            ],
        ),
    ]
