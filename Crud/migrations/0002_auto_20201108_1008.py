# Generated by Django 2.2.9 on 2020-11-08 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='message_en',
            field=models.TextField(help_text="what's on your mind ...", null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='message_hi',
            field=models.TextField(help_text="what's on your mind ...", null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.CharField(help_text='title of message.', max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_hi',
            field=models.CharField(help_text='title of message.', max_length=120, null=True),
        ),
    ]
