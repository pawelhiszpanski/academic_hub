from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import ResourceForm

# Create your views here.
def index(request):
    user_profile = None
    if request.user.is_authenticated:
        user_profile, is_created = Profile.objects.get_or_create(user=request.user) # it returns 1. user and 2. if was created(?)
    fields = FieldOfStudy.objects.all()
    context = {
        'fields': fields,
        'profile': user_profile,
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

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')

        form = ResourceForm(request.POST)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.subject = subject
            resource.save()
            return redirect('subject_resources', subject_id=subject.id)
    else:
        form = ResourceForm()

    context = {
        'subject': subject,
        'resources': resources,
        'form': form,
    }
    return render(request, 'resources/subject_resources.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'resources/register.html', {'form': form})