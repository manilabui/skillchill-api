# Generated by Django 3.0.4 on 2020-03-18 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skillchillapi', '0007_auto_20200317_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='modified_at',
            field=models.DateTimeField(null=True),
        ),
    ]