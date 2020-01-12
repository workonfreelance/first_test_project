from django.db import models
from django.forms import forms, ModelForm
from django.urls import reverse
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(default="None",verbose_name="Картинка")

    def __str__(self):
        return self.name


class Job(models.Model):
    job_name = models.TextField(max_length=50,verbose_name="Название вакансии")
    short_job_name = models.TextField(max_length=50,verbose_name="Краткое название вакансии")
    tags = models.ManyToManyField(Tag,verbose_name="Теги")
    loacation = models.TextField(max_length=50,verbose_name="Местонахождение")
    hot = models.BooleanField(default=False,verbose_name="Hot")
    body = models.TextField(default="",verbose_name="Описание")

    class Meta:
        ordering = ('hot',)




