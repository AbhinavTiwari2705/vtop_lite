# Generated by Django 3.2.7 on 2023-02-02 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_s_school_student_s_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Droupout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=100)),
                ('s_email', models.EmailField(max_length=100)),
            ],
        ),
    ]
