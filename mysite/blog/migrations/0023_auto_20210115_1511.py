# Generated by Django 3.1.3 on 2021-01-15 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20201208_2025'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['pub_date']},
        ),
    ]
