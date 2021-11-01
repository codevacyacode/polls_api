# Generated by Django 2.2.10 on 2021-11-01 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20211004_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='choice',
            field=models.CharField(max_length=255, verbose_name='Выбранный вариант'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='respondent',
            field=models.CharField(max_length=255, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='question',
            name='option0',
            field=models.CharField(blank=True, max_length=62, null=True, verbose_name='Вариант ответа А'),
        ),
        migrations.AlterField(
            model_name='question',
            name='option1',
            field=models.CharField(blank=True, max_length=62, null=True, verbose_name='Вариант ответа Б'),
        ),
        migrations.AlterField(
            model_name='question',
            name='option2',
            field=models.CharField(blank=True, max_length=62, null=True, verbose_name='Вариант ответа В'),
        ),
        migrations.AlterField(
            model_name='question',
            name='option3',
            field=models.CharField(blank=True, max_length=62, null=True, verbose_name='Вариант ответа Г'),
        ),
    ]