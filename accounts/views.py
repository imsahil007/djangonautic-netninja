from django.shortcuts import redirect,render
# from . import views
# from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #login the user
            login(request, user)
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    #form is not valid or GET
    return render(request, 'accounts/signup.html',{"form": form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # form.save()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))

            return redirect('articles:list')
            # #login the user
            # return redirect('articles:list')
    else:
        form = AuthenticationForm()
    #form is not valid or GET
    return render(request, 'accounts/login.html',{"form": form})


def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('articles:list')
