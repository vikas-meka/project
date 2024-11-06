# Generated by Django 4.2.6 on 2023-10-12 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=150)),
                ('course', models.CharField(max_length=150)),
                ('ct1', models.IntegerField(blank=True)),
                ('ct2', models.IntegerField(blank=True)),
                ('end', models.IntegerField(blank=True)),
                ('internals', models.IntegerField(blank=True)),
                ('grade', models.IntegerField(blank=True)),
                ('score', models.CharField(blank=True, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=128)),
                ('course1', models.CharField(max_length=150)),
            ],
        ),
    ]
