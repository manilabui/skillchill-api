# Generated by Django 3.0.4 on 2020-03-17 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skillchillapi', '0006_auto_20200317_0640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postpage',
            name='modified_at',
            field=models.DateTimeField(null=True),
        ),
    ]
