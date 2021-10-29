from django.shortcuts import render, redirect
from .models import Project, Profile
from .forms import ProjectForm, ProfileUpdateForm, UserUpdateForm
from django.contrib import messages


# Create your views here.
def home(request):
    projects=Project.objects.all()
    photos=Project.objects.all()
    context={'photos':photos, 'projects':projects}
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

def viewProject(request):
    image=Project.objects.filter()
    context={'image':image}
    return render(request, 'all-awards/project.html', context)

def search_results(request):

    if 'author' in request.GET and request.GET["author"]:
        search_term = request.GET.get("author")
        searched_profiles = Project.search_by_author(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"searched_profiles": searched_profiles})

    else:
        message = "You haven't searched for any person"
        return render(request, 'search.html',{"message":message})

def profile(request):
    user = request.user
    user = Profile.objects.get_or_create(user= request.user)
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)                         
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated successfully!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'user': user

    }

    return render(request, 'all-awards/profile.html', context)