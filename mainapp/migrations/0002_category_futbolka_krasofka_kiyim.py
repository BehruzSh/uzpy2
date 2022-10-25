# Generated by Django 4.0.2 on 2022-07-03 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Futbolka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=200)),
                ('ulcham', models.CharField(max_length=200)),
                ('narxi', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Krasofka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=200)),
                ('ulcham', models.CharField(max_length=200)),
                ('narxi', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Kiyim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=200)),
                ('ulcham', models.CharField(max_length=200)),
                ('narxi', models.CharField(max_length=200)),
                ('turi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category')),
            ],
        ),
    ]