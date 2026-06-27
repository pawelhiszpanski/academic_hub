from django.shortcuts import render
from .models import *
from django.db.models import Q

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

    selected_stream = request.GET.get('stream', 'ALL')

    subjects = Subject.objects.filter(field_of_study=field, semester=semester_id, stream=selected_stream)
    context = {
        'field': field,
        'subjects': subjects,
        'semester_number': semester_id,
        'selected_stream': selected_stream,
    }
    return render(request, 'resources/semester_detail.html', context)

def subject_resources(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    resources = subject.resources.all()
    context = {
        'subject': subject,
        'resources': resources,
    }
    return render(request, 'resources/subject_resources.html', context)