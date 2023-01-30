# Generated by Django 3.2.7 on 2023-01-30 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=100)),
                ('s_current_sem', models.CharField(max_length=100)),
                ('s_address', models.CharField(max_length=100)),
                ('s_school', models.CharField(max_length=100)),
                ('s_email', models.EmailField(max_length=100)),
            ],
        ),
    ]