# Generated by Django 4.2.6 on 2023-10-25 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_delete_mark_marks_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marks',
            name='total',
        ),
    ]
