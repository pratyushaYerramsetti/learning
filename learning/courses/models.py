from django.db import models
# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length = 32)
    class Meta:
        verbose_name_plural = "Courses"


    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
type_choices =  (
    ('CSE' , 'cse'),
    ('ECE' , 'ece'),
    ('EEE' , 'eee'),
    ('IT' , 'it'),
)
class Book(models.Model):
    class Meta:
        verbose_name_plural = "Books"


    title = models.CharField(max_length = 32)
    description = models.FileField(upload_to='page' ,null=True, blank=True)
    author = models.CharField(max_length = 32)
    date = models.DateField()
    branch = models.CharField(max_length = 6, choices = type_choices)

    def __str__(self):
        return "title = {} ,author = {},date = {},branch = {} ".format(self.title,self.author,self.date,self.branch)
