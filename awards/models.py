from django.db import models


# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=30)
    image=models.ImageField()
    description=models.TextField()
    link=models.URLField(max_length=200)

    def __str__(self):
        return f'{self.title.username}'

class Profile(models.Model):
    picture=models.ImageField()
    bio=models.TextField(max_length=100)
    projects=models.ForeignKey('Project',related_name='links',on_delete=models.CASCADE)
    contact=models.CharField(max_length=10)

    def __str__(self):
        return self.picture