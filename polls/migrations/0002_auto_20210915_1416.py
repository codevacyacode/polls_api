# Generated by Django 2.2.10 on 2021-09-15 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='option0',
            field=models.CharField(default='Да', max_length=64, verbose_name='Вариант ответа А'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='option1',
            field=models.CharField(default='Нет', max_length=64, verbose_name='Вариант ответа Б'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='option2',
            field=models.CharField(default='Возможно', max_length=64, verbose_name='Вариант ответа В'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='option3',
            field=models.CharField(default='Затрудняюсь ответить', max_length=64, verbose_name='Вариант ответа Г'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='poll',
            name='date_a',
            field=models.DateField(verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='date_b',
            field=models.DateField(verbose_name='Дата завершения'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='question',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Poll', verbose_name='Опрос'),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('FC', 'Свободная формулировка ответа'), ('OO', 'Выбор одного варианта ответа'), ('MO', 'Выбор нескольких вариантов ответа')], max_length=2, verbose_name='Тип вопроса'),
        ),
    ]
