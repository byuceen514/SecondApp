from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'life/home.html', context)

def help(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'life/Help.html', context)

def documentation(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'life/Documentation.html', context)