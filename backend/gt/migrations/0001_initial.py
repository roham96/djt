# Generated by Django 4.0.4 on 2022-04-15 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('destination', models.TextField()),
                ('path', models.CharField(max_length=200)),
            ],
        ),
    ]
