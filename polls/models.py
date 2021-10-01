from django.db import models

# Create your models here.
class Poll(models.Model):
    title = models.CharField(max_length = 128, verbose_name = 'Название')
    date_a = models.DateField(verbose_name = 'Дата начала')
    date_b = models.DateField(verbose_name = 'Дата завершения')
    description = models.TextField(null = True, blank = True, verbose_name = 'Описание')
    
    class Meta:
        verbose_name_plural = 'Опросы'
        verbose_name = 'Опрос'
        ordering = ['-date_a']
    
class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete = models.CASCADE, verbose_name = 'Опрос')
    title = models.CharField(max_length = 128, verbose_name = 'Вопрос')
    FREECHOICE = 'FC'
    ONEOPTION = 'OO'
    MULTIPLEOPTIONS = 'MO'
    QUESTION_TYPE_CHOICES = [
        (FREECHOICE, 'Свободная формулировка ответа'),
        (ONEOPTION, 'Выбор одного варианта ответа'),
        (MULTIPLEOPTIONS, 'Выбор нескольких вариантов ответа'),
    ]
    type = models.CharField(
        max_length = 2,
        choices = QUESTION_TYPE_CHOICES,
        verbose_name = 'Тип вопроса',
    )
    option0 = models.CharField(max_length = 64, verbose_name = 'Вариант ответа А', null = True, blank = True)
    option1 = models.CharField(max_length = 64, verbose_name = 'Вариант ответа Б', null = True, blank = True)
    option2 = models.CharField(max_length = 64, verbose_name = 'Вариант ответа В', null = True, blank = True)
    option3 = models.CharField(max_length = 64, verbose_name = 'Вариант ответа Г', null = True, blank = True)
    
    class Meta:
        verbose_name_plural = 'Вопросы'
        verbose_name = 'Вопрос'
        ordering = ['-poll']
        
class Answer(models.Model):
    user = models.CharField(max_length = 32, verbose_name = 'Пользователь')
    poll = models.ForeignKey(Poll, on_delete = models.CASCADE, verbose_name = 'Опрос')
    question = models.ForeignKey(Question, on_delete = models.CASCADE, verbose_name = 'Вопрос')
    choice = models.CharField(max_length = 64, verbose_name = 'Выбранный вариант')
    
    class Meta:
        verbose_name_plural = 'Ответы'
        verbose_name = 'Ответ'
        ordering = ['-user']