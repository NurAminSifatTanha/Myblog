# Generated by Django 2.2.2 on 2019-06-15 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pub_date']},
        ),
    ]
