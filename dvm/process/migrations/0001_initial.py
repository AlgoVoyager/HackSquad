# Generated by Django 4.2.6 on 2023-11-21 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='voter_Details',
            fields=[
                ('voter_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('mobile', models.CharField(max_length=15)),
                ('is_voted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'voter',
                'verbose_name_plural': 'voters',
                'ordering': ('name',),
            },
        ),
    ]
