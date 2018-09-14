from django.shortcuts import render, render_to_response
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.http import HttpResponse
# from . import models
from courses.models import Book,Course


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def books_list(request):
        books_lists = Book.objects.filter(branch='CSE').order_by('date','title')
        return render(request, 'cse.html', {'books': books_lists})
        # return HttpResponse("hey")

def displayDate():
    print("hello")
        
