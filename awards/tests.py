from django.test import TestCase
from .models import Profile, Project

# Create your tests here.
class ProjectTestClass(TestCase):
    #set up method
    def setUp(self):
        self.sharry=Project(author='sharry', title='Instaclone', description='app looks like instagram')