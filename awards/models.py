from django.db import models
from django.db.models.deletion import CASCADE
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE,related_name='author')
    title=models.CharField(max_length=30)
    image=models.ImageField()
    description=models.TextField()
    link=models.URLField(max_length=200)

    def create_project(self):
        self.save()

    def save_project(self):
        self.save()

    def __str__(self):
        return f'{self.title}'

class Profile(models.Model):
    user=models.OneToOneField('auth.user',on_delete=models.CASCADE)
    picture=models.ImageField()
    bio=models.TextField(max_length=100)
    projects=models.ForeignKey('Project',related_name='links',on_delete=models.CASCADE)
    contact=models.CharField(max_length=10)

    def save_profile(self):
        self.save()

    def __str__(self):
        return self.user
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Rating(models.Model):
    RATING_CHOICES   = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings', null=True)
    design_rating = models.PositiveIntegerField(choices=RATING_CHOICES, default=0)
    usability_rating = models.PositiveIntegerField(choices=RATING_CHOICES, default=0)
    content_rating = models.PositiveIntegerField(choices=RATING_CHOICES, default=0)
    date_posted = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
            return self.author
    def save_comment(self):
            self.save()

    def get_comment(self, id):
            comments = Rating.objects.filter(project_id=id)
            return comments
            
@classmethod
def get_ratings(cls):
        ratings = Rating.objects.all()
        return ratings

# class Ratings(models.Model):
#     author=models.ForeignKey('auth.user',on_delete=models.CASCADE)
#     project=models.ForeignKey('Project', on_delete=models.CASCADE)
#     design_rating=models.PositiveIntegerField()
#     usability_rating=models.PositiveIntegerField()
#     content_rating=models.PositiveIntegerField()

#     Rating_choices=(

#     )
# @classmethod
# def get_ratings(cls):
#     ratings=Ratings.objects.all()
#     return ratings
