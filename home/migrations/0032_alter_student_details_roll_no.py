# Generated by Django 4.2.6 on 2023-11-02 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_alter_teacher_course1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_details',
            name='roll_no',
            field=models.CharField(max_length=150, primary_key=True, serialize=False, unique=True),
        ),
    ]