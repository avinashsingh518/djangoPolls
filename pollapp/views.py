from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Question, Choice

# Create your views here.
def index(request):
    questions = Question.objects.all()
    return render(request, 'index.html', {'questions': questions})

def vote(request,pk):
    question = Question.objects.get(id=pk)
    options = question.choices.all()
    # if request.method == 'POST':
    #     inputvalue = request.POST['choice']
    #     selection_option = options.get(id=inputvalue)
    #     selection_option.vote += 5
    #     selection_option.save()

    return render(request, 'vote.html', {'question':question, 'options': options })

def result(request, pk):
    question = Question.objects.get(id=pk)
    options = question.choices.all()
    if request.method == 'POST':
        inputvalue = request.POST['choice']
        selection_option = options.get(id=inputvalue)
        selection_option.vote += 5
        selection_option.save()
    return render(request, 'result.html', {'question': question, 'options': options})



def profile(request):
    return render(request, 'profile.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        x = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email,
                                     password=password)
        x.save()
        print("user created successfully")
        return redirect("/index")
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/index')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

