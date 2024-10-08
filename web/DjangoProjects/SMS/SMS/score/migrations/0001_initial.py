# Generated by Django 4.0.1 on 2022-01-14 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(db_index=True, default=True, help_text='状态')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='更新时间')),
                ('title', models.CharField(help_text='title/考试名称', max_length=20, verbose_name='考试名称')),
                ('score', models.DecimalField(decimal_places=2, help_text='score/分数', max_digits=5, verbose_name='分数')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student', verbose_name='学生姓名')),
            ],
            options={
                'verbose_name': '成绩信息',
                'verbose_name_plural': '成绩信息',
                'db_table': 'score',
            },
        ),
    ]
