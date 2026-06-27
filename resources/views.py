from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    fields = FieldOfStudy.objects.all()
    context = {
        'fields': fields,
    }
    return render(request, 'resources/index.html', context)

def field_detail(request, field_id):
    field = FieldOfStudy.objects.get(id=field_id)
    context = {
        'field': field,
    }
    return render(request, 'resources/field_detail.html', context)

def semester_detail(request, field_id, semester_id):
    field = FieldOfStudy.objects.get(id=field_id)
    subjects = Subject.objects.filter(field_of_study=field, semester=semester_id)
    context = {
        'field': field,
        'subjects': subjects,
        'semester_number': semester_id,
    }
    return render(request, 'resources/semester_detail.html', context)