# Generated by Django 5.0.3 on 2024-05-07 05:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('file_name', models.CharField(max_length=255)),
                ('number_of_records', models.IntegerField(default=0)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('data_type', models.CharField(max_length=50)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='columns', to='edgar.file')),
            ],
            options={
                'unique_together': {('file', 'name')},
            },
        ),
    ]
