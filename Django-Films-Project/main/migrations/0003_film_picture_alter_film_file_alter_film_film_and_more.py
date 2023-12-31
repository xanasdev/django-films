# Generated by Django 4.2.3 on 2023-08-17 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_users_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='picture',
            field=models.FileField(null=True, upload_to='films/pictures'),
        ),
        migrations.AlterField(
            model_name='film',
            name='file',
            field=models.FileField(upload_to='films/videos/'),
        ),
        migrations.AlterField(
            model_name='film',
            name='film',
            field=models.CharField(default='a52e6e9e-3017-4eff-9854-24dbcb1ed1d5', max_length=256, verbose_name='Уникальный UUID4'),
        ),
        migrations.AlterField(
            model_name='users',
            name='userid',
            field=models.CharField(default='a52e6e9e-3017-4eff-9854-24dbcb1ed1d5', max_length=256, verbose_name='Пользовательский ID'),
        ),
    ]
