from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm


def signup(request):
    '''Signs a user in'''
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = form.save()
            login(request, user)

            return redirect("webapp:index")

    else:
        form = SignUpForm()

    return render(request, "accounts/signup.html", {"form": form})
