from django.shortcuts import render, redirect
from .models import PostModel
from .forms import PostModelForm
# import  get_object_or_404
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    posts = PostModel.objects.all()
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            user = get_object_or_404(User, username=request.user)
            instance.author = request.user
            instance.save()
            return redirect('index')
    else:
        form = PostModelForm()
        print(request.user)

    context = {
        'posts': posts,
        'form': form,

    }

    return render(request, 'blog/index.html', context)


