# Generated by Django 4.0.1 on 2022-01-14 02:54

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
            name='Teacher',
            fields=[
                ('status', models.BooleanField(db_index=True, default=True, help_text='状态')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='更新时间')),
                ('tid', models.IntegerField(primary_key=True, serialize=False, verbose_name='老师ID')),
                ('name', models.CharField(help_text='name/姓名', max_length=20, verbose_name='姓名')),
                ('email', models.CharField(help_text='email/邮箱', max_length=60, unique=True, verbose_name='邮箱')),
                ('class_name', models.CharField(help_text='class_name/班级名称', max_length=50, verbose_name='班级名称')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', help_text='gender/性别', max_length=32, verbose_name='性别')),
                ('phone', models.CharField(help_text='phone/手机号', max_length=11, unique=True, verbose_name='手机号')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '老师信息',
                'verbose_name_plural': '老师信息',
                'db_table': 'teacher',
            },
        ),
    ]
