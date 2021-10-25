from django.shortcuts import render
from .models import Project, Profile

# Create your views here.
def home(request):
    projects=Project.objects.all()
    photos=Project.objects.all()
    context={'projects':projects, 'photos':photos}
    return render(request, 'all-awards/home.html', context)