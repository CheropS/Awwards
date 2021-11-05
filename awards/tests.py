from django.test import TestCase
from .models import Profile, Project

# Create your tests here.
class ProjectTestClass(TestCase):
    #set up method
    def setUp(self):
        self.sharry=Project(title='Instaclone', description='app looks like instagram')
    
    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.sharry, Project))

    #testing saving method
    def test_save_method(self):
        self.sharry.save_project()
        projects=Project.objects.all()
        self.assertTrue(len(projects)> 0)

