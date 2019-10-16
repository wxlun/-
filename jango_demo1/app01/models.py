from django.db import models

class Classes(models.Model):
    titile=models.CharField(max_length=32)
    m=models.ManyToManyField("Teachers")

class Teachers(models.Model):
    name=models.CharField(max_length=32)


class Student(models.Model):
    username=models.CharField(max_length=32)
    age=models.IntegerField()
    gender=models.BooleanField()
    cs=models.ForeignKey(Classes,on_delete=True)
