from django.db import models

# Create your models here.
class Xaridor(models.Model):
    ism=models.CharField(max_length=200)
    familya=models.CharField(max_length=200)
    parol=models.CharField(max_length=200)
    def __str__(self):
        return self.ism
class Futbolka(models.Model):
    nomi=models.CharField(max_length=200)
    ulcham=models.CharField(max_length=200)
    narxi=models.CharField(max_length=200)
    def __str__(self):
        return self.nomi
class Krasofka(models.Model):
    nomi=models.CharField(max_length=200)
    ulcham=models.CharField(max_length=200)
    narxi=models.CharField(max_length=200)
    def __str__(self):
        return self.nomi
class Category(models.Model):
    nomi=models.CharField(max_length=200)
    def __str__(self):
        return self.nomi
class Kiyim(models.Model):
    nomi=models.CharField(max_length=200)
    turi=models.ForeignKey(Category,on_delete=models.CASCADE)
    ulcham=models.CharField(max_length=200)
    narxi=models.CharField(max_length=200)
    def __str__(self):
        return self.nomi