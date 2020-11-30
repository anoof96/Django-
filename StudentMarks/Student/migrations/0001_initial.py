# Generated by Django 3.1.3 on 2020-11-14 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('standard', models.PositiveSmallIntegerField()),
                ('sex', models.CharField(choices=[(1, 'F'), (2, 'M')], max_length=1)),
            ],
        ),
    ]