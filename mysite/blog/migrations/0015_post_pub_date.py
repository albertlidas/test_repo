# Generated by Django 3.1.3 on 2020-11-26 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20201125_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]