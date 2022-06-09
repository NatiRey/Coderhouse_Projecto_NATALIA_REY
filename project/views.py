import random
import string
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.shortcuts import render

from project.models import Project
from project.forms import ProjectForm


def project_list(request):
    project = Project.objects.all()

    context_dict = {
        '': project
    }

    return render(
        request=request,
        context=context_dict,
        template_name="project/project_list.html"
    )


@login_required
def project_form(request):
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            data = project_form.cleaned_data

            # Una pequeña muestra de procesos de unit test
            KEY_LEN = 20
            char_list = [
                random.choice((string.ascii_letters + string.digits))
                for _ in range(KEY_LEN)
            ]
            mock_name = ''.join(char_list)
            print(f'----------> Try: {mock_name}')

            project = Project(
                name=mock_name,
                type=data['type'],
                description=data['description'],
            )
            project.save()

            projects = project.objects.all()
            context_dict = {
                'projects': projects
            }
            return render(
                request=request,
                context=context_dict,
                template_name="project/project_list.html"
            )

    project_form = ProjectForm(request.POST)
    context_dict = {
        'project_form': project_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='project/project_form.html'
    )


@login_required
def update_project(request, pk: int):
    project = Project.objects.get(pk=pk)

    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            data = project_form.cleaned_data
            project.name = data['name']
            project.type = data['type']
            project.description = data['description']
            project.save()

            projects = Project.objects.all()
            context_dict = {
                'projects': projects
            }
            return render(
                request=request,
                context=context_dict,
                template_name="project/project_list.html"
            )

    project_form = ProjectForm(model_to_dict(project))
    context_dict = {
        'project': project,
        'project_form': project_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='project/project_form.html'
    )


@login_required
def delete_project(request, pk: int):
    project = Project.objects.get(pk=pk)
    if request.method == 'POST':
        project.delete()

        projects = Project.objects.all()
        context_dict = {
            'projects': projects
        }
        return render(
            request=request,
            context=context_dict,
            template_name="project/project_list.html"
        )

    context_dict = {
        'project': project,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='project/project_confirm_delete.html'
    )
