from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http import HttpResponse, JsonResponse
from filetransfers.api import serve_file

from .forms import UserLoginForm, UserRegisterForm, User
from .models import Category, ResFile, IsFavourite



# Create your views here.
@login_required
def index(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories,
        'index' : True,
    }
    return render(request, 'Resource/index.html', context)

@login_required
def category_view(request, category_id):
    req_category = get_object_or_404(Category, pk= category_id)
    files = ResFile.objects.filter(category=req_category)
    context = {
        'files' : files,
        'title' : req_category.category,
        'index' : True,
    }
    return render(request, 'Resource/category_view.html', context)

@login_required
def all_files_view(request):
    files = ResFile.objects.all()
    context = {
        'files' : files,
        'title' : 'All Files',
        'index' : True,
    }
    return render(request, 'Resource/category_view.html', context)


class FileCreate(LoginRequiredMixin, CreateView):
    model = ResFile
    fields = ['title', 'description', 'category', 'tags', 'file']
    def form_valid(self, form):
        form.instance.uploader = self.request.user
        return super().form_valid(form)
    
def login_view(request):
    current_user = request.user
    if current_user.is_authenticated:
        return redirect('Resource:index')
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        
        login(request, user)
        
        if next:
            return redirect(next)
        return redirect('Resource:index')
    
    context = {
        'form': form,
    }
    return render(request, 'Resource/login.html', context)


def register_view(request):
    current_user = request.user
    if current_user.is_authenticated:
        return redirect('Resource:index')
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        
        if next:
            return redirect(next)
        return redirect('Resource:index')
    
    context = {
        'form': form,
    }
    return render(request, 'Resource/signup.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('Resource:index')


@login_required
def is_favourite(request, file_id):
    current_user = request.user
    current_file = get_object_or_404(ResFile, pk=file_id)
    p, created = IsFavourite.objects.get_or_create(
    file = current_file,
    user = current_user,
    )
    if created:
        p.save()
    else:
        p.delete()
    return JsonResponse(
        {"status":"success"}
    )

@login_required
def favourite_view(request):
    current_user = request.user
    filess = IsFavourite.objects.filter(user=current_user)
    files = []
    for f in filess:
        files.append(f.file)
    context = {
        'files' : files,
        'title' : 'My Favourites',
        'favourite_view' : True,
    }
    return render(request, 'Resource/category_view.html', context)

@login_required
def my_uploads(request):
    current_user = request.user
    files = ResFile.objects.filter(uploader=current_user)
    context = {
        'files' : files,
        'title' : 'My Uploads',
        'upload_view' : True,
    }
    return render(request, 'Resource/category_view.html', context)

@login_required
def download(request, file_id):
    upload = get_object_or_404(ResFile, pk=file_id)
    return serve_file(request, upload.file)
    