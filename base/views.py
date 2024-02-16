from django.shortcuts import render
from django.http import HttpResponse
from .models import Mentor


def home(request):
    return render(request, 'base/home.html')

def card(request, pk): 
    mentor = Mentor.objects.get(id=pk)
    context = {'mentor':mentor}
    # mentor = {'names':'Alexia Benett', 'company':'Dow Chemical','job_title':'Software Engineer', 'specializations':'Artificial Intelligence'}
    return render(request, 'base/mentor_card.html', context)


def dashboard(request):
    mentors = Mentor.objects.all()
    context = {'mentors':mentors}
    return render(request, 'base/mentee_dashboard.html',context)
