# Generated by Django 2.2.16 on 2020-10-05 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20201005_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='uploads/1.png', upload_to='uploads/'),
        ),
    ]
