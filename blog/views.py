from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Project
from . import models
from django.utils import timezone
# Create your views here.
from .forms import new_project_form
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # <-- Here
import requests
import json


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
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = new_project_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.cleaned_data

            a = requests.post("http://localhost:8000/api-token-auth/?format=json",
                              data={"username": data['username'], "password": data['password']})
            dataf = json.loads(a.text)
            headers = {'Authorization': f'Token {dataf["token"]}'}
            if requests.get('http://localhost:8000/keyauth', headers=headers).json()['isAdmin']:

                ar = Project.objects.create(
                    title=data['project_title'], content=data['project_text'], date_posted=timezone.now(), category=data['project_category'])
                ar.save()
                messages.success(request, 'your project has been posted')
        return render(request, 'blog/writer.html', {'form': new_project_form})

    else:
        return render(request, 'blog/writer.html', {'form': new_project_form})
