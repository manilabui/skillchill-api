# Generated by Django 3.0.4 on 2020-03-16 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skillchillapi', '0003_auto_20200315_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.RemoveField(
            model_name='postpage',
            name='post_type',
        ),
        migrations.RemoveField(
            model_name='userskill',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='skillager',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='skillchillapi.Skillager'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='skillchillapi.PostType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='skillager',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='skillchillapi.Skillager'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userskill',
            name='skillager',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='skillchillapi.Skillager'),
            preserve_default=False,
        ),
    ]
