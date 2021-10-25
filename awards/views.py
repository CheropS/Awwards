from django.shortcuts import render, redirect
from .models import Project, Profile
from .forms import ProjectForm


# Create your views here.
def home(request):
    projects=Project.objects.all()
    photos=Project.objects.all()
    context={'projects':projects, 'photos':photos}
    return render(request, 'all-awards/home.html', context)

def create_post(request):
    current_user = request.user
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid:
            post = form.save(commit= False)
            post.author = current_user
            post.save()
        return redirect('home')
    else:
        form = ProjectForm()
    return render(request,'all-awards/new.html',{'form':form})