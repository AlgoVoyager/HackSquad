# Generated by Django 4.2.6 on 2023-12-01 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0005_voteends'),
    ]

    operations = [
        migrations.AddField(
            model_name='oppositions',
            name='party_symbol',
            field=models.ImageField(default='default.jpg', upload_to='partySymbol'),
        ),
    ]
