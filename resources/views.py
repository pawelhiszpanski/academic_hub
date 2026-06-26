from django.shortcuts import render
from .models import FieldOfStudy

# Create your views here.

def index(request):
    fields = FieldOfStudy.objects.all()

    context = {
        'fields': fields,
    }

    return render(request, 'resources/index.html', context)