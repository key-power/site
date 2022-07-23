from django.shortcuts import render
from .models import Header,Skills,Settings,Reviews,Team,TypeWorks,Works,Partners
# Create your views here.
def homme(request):
    return render(request, 'index.html',{
        "header":Header.objects.all(),
        "skills":Skills.objects.all(),
        "settings":Settings.objects.first(),
        "reviews":Reviews.objects.all(),
        "team":Team.objects.all(),
        "works":Works.objects.all(),
        "typeworks":TypeWorks.objects.all(),
        "partners":Partners.objects.all()


    })