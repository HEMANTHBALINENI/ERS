# Generated by Django 3.0 on 2020-03-12 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GRSapp', '0011_auto_20200309_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersmodal',
            name='user_pic',
            field=models.ImageField(default='ImageNotFound', upload_to='user_pics/'),
        ),
    ]
