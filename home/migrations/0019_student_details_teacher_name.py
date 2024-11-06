# Generated by Django 4.2.6 on 2023-11-01 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_marks_branch_marks_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(blank=True, max_length=150, null=True)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('year', models.CharField(blank=True, max_length=2, null=True)),
                ('branch', models.CharField(blank=True, max_length=4, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='teacher',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
