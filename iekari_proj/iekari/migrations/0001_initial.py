# Generated by Django 2.2.1 on 2021-08-20 07:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('age', models.IntegerField(verbose_name='年齢')),
                ('gender', models.IntegerField(choices=[(0, '男性'), (1, '女性')], verbose_name='性別')),
                ('household_num', models.IntegerField(verbose_name='世帯人数')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
            options={
                'verbose_name': 'ユーザー情報データ',
                'verbose_name_plural': 'ユーザー情報データ',
            },
        ),
    ]