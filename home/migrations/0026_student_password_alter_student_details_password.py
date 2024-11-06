# Generated by Django 4.2.6 on 2023-11-02 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_alter_student_details_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_password',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=150, null=True)),
                ('password', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='student_details',
            name='password',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
