# Generated by Django 4.2.7 on 2023-11-02 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Название задания')),
                ('is_complete', models.BooleanField(default=False, verbose_name='Заваершено ')),
            ],
            options={
                'verbose_name': 'Задание ',
                'verbose_name_plural': 'Задания ',
            },
        ),
    ]
