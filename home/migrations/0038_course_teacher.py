# Generated by Django 4.2.6 on 2023-11-08 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_rename_admin_details_admin_detail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.CharField(blank=True, default='abc', max_length=150, null=True),
        ),
    ]