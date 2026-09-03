from django.shortcuts import render

# apps\profiles\views.py
# Create your views here.


def index(request):
    return render(request, 'profiles/profile.html')
