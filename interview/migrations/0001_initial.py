# Generated by Django 3.1.6 on 2021-02-18 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generation', models.IntegerField(blank=True, default=0, null=True, verbose_name='기수')),
                ('question1', models.CharField(blank=True, max_length=155, null=True, verbose_name='질문1')),
                ('question2', models.CharField(blank=True, max_length=155, null=True, verbose_name='질문2')),
                ('question3', models.CharField(blank=True, max_length=155, null=True, verbose_name='질문3')),
                ('question4', models.CharField(blank=True, max_length=155, null=True, verbose_name='질문4')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generation', models.IntegerField(blank=True, default=0, null=True, verbose_name='기수')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='이름')),
                ('major', models.CharField(blank=True, choices=[('double_major', '복수전공자'), ('non_major', '비전공자'), ('major', '전공자')], max_length=50, null=True, verbose_name='전공여부')),
                ('intro', models.TextField(blank=True, null=True, verbose_name='썸네일용 간단한 소개')),
                ('image', models.ImageField(blank=True, null=True, upload_to='interview', verbose_name='썸네일용 사진')),
                ('answer1', models.TextField(blank=True, null=True, verbose_name='답변(내용) 1')),
                ('answer2', models.TextField(blank=True, null=True, verbose_name='답변(내용) 2')),
                ('answer3', models.TextField(blank=True, null=True, verbose_name='답변(내용) 3')),
                ('answer4', models.TextField(blank=True, null=True, verbose_name='답변(내용) 4')),
                ('asking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.asking')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]