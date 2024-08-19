# Generated by Django 5.1 on 2024-08-19 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('description', models.TextField(verbose_name='описание')),
            ],
            options={
                'verbose_name': 'Машина',
                'verbose_name_plural': 'машины',
            },
        ),
    ]
