from .forms import new_project_form
from django.core.files.storage import default_storage
from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Project
from . import models
from django.utils import timezone
from .forms import new_project_form
from .forms import new_project_form
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # <-- Here
import json
import os
from django.contrib.auth.models import User
from django.views import View
from django.http import JsonResponse

from django_backend.custom_storages import MediaStorage


def Projects(request, **kwargs):
    unrestricted_articles = []
    projects = []
    for project in Project.objects.all().order_by('-date_posted'):
        if project.category == kwargs.get('category'):
            projects.append(project)

    context = {
        'Projects': projects
    }

    return render(request, 'blog/projects.html', context)


class keyauth(APIView):
    permission_classes = (IsAuthenticated,)             # <-- And here

    def get(self, request):
        content = {
            'authenticated': True,
            'detail': 'success',
            'user': str(request.user.username),
            'isAdmin': request.user.groups.filter(name='admin').count() == 1,
        }
        return Response(content)


def writer(request):
    messages.info(request, default_storage.connection)
    if request.method == 'POST':
        file = default_storage.open('storage_test', 'w')
        file.write('storage contents')
        file.close()
        messages.success(request, 'you sent a POST requuest')
        # create a form instance and populate it with data from the request:
        form = new_project_form(request.POST, files=request.FILES)
        if form.is_valid():
            messages.success(request, 'form is valid')

            data = form.cleaned_data

            if data['key'] == os.environ.get('postkey'):
                messages.success(request, ' your password is correct')
                ar = Project.objects.create(title=data['project_title'], content=data['project_text'], date_posted=timezone.now(
                ), category=data['project_category'], video=request.FILES['project_video'])
                ar.save()
                messages.success(request, 'your project has been posted')
            else:
                messages.warning(request, 'Auth Failed')
        return render(request, 'blog/writer.html', {'form': new_project_form})

    else:
        return render(request, 'blog/writer.html', {'form': new_project_form})


# def writer(request):
#     lastvideo = Project.objects.last()
#     videofile = lastvideo.video
#     form = new_project_form(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.date_posted = timezone.now()
#         form.save(date_posted=timezone.now())
#
#     context = {'videofile': videofile,
#                'form': form,
#                'time': timezone.now()
#                }
#
#     return render(request, 'blog/writer.html', context)
