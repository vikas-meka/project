# Generated by Django 4.2.6 on 2023-10-26 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_grade_roll_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='cgpa',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='grade',
            name='roll_no',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
