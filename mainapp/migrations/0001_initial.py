# Generated by Django 4.0.2 on 2022-07-03 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Xaridor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=200)),
                ('familya', models.CharField(max_length=200)),
                ('parol', models.CharField(max_length=200)),
            ],
        ),
    ]