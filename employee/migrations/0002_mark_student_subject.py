# Generated by Django 3.1 on 2022-07-17 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mid', models.IntegerField()),
                ('sid', models.IntegerField()),
                ('sub_id', models.IntegerField()),
                ('mark', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'mark',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_id', models.IntegerField()),
                ('sub_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'subject',
            },
        ),
    ]