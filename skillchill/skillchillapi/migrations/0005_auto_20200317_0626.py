# Generated by Django 3.0.4 on 2020-03-17 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skillchillapi', '0004_auto_20200316_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('P', 'Photo'), ('T', 'Text'), ('V', 'Video'), ('L', 'Link')], max_length=1),
        ),
        migrations.DeleteModel(
            name='PostType',
        ),
    ]
