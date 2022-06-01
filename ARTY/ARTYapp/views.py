from django.shortcuts import render
from django.db.models import Q
from django.forms.models import model_to_dict

from ARTYapp.models import Profile, Project, Stock
from ARTYapp.forms import Profile_form, Project_form, Stock_form


def index(request):
    return render(request, "templates\index.html")


def profile(request):
    profile = Profile.objects.all()

    context_dict = {
        'profile': profile
    }

    return render(
        request=request,
        context=context_dict,
        template_name="templates/profiles.html"
    )

def project(request):
    projects = Project.objects.all()

    context_dict = {
        'projects': projects
    }

    return render(
        request=request,
        context=context_dict,
        template_name="templates/projects.html"
    )

def stock(request):
    stock = Stock.objects.all()

    context_dict = {
        'stock': stock
    }

    return render(
        request=request,
        context=context_dict,
        template_name="template/stocks.html")

#def form_hmtl(request):
#
#    if request.method == 'POST':
#        project = Project(name=request.POST['name'], code=request.POST['code'])
#        course.save()

#        courses = Course.objects.all()
#        context_dict = {
#            'courses': courses
#        }

#        return render(
#            request=request,
#            context=context_dict,
#            template_name="app_coder/courses.html"
#        )

#    return render(
#        request=request,
#        template_name='app_coder/formHTML.html'
#    )


#def course_forms_django(request):
#    if request.method == 'POST':
#        course_form = CourseForm(request.POST)
#        if course_form.is_valid():
#            data = course_form.cleaned_data
#            course = Course(name=data['name'], code=data['code'])
#            course.save()

#            courses = Course.objects.all()
#            context_dict = {
#                'courses': courses
#           }
#            return render(
#                request=request,
#                context=context_dict,
#                template_name="app_coder/courses.html"
#            )

#    course_form = CourseForm(request.POST)
#    context_dict = {
#        'course_form': course_form
#    }
#    return render(
#        request=request,
#        context=context_dict,
#        template_name='app_coder/course_django_forms.html'
#    )


def profile_forms_django(request):
    if request.method == 'POST':
        profile_form = Profile_form(request.POST)
        if profile_form.is_valid():
            data = profile_form.cleaned_data
            profile = Profile(
                name=data['name'],
                last_name=data['last_name'],
                email=data['email'],
                artist_name=data['artist_name'],
                country=data['country'],
            )
            profile.save()

            profiles = Profile.objects.all()
            context_dict = {
                'profiles': profiles
            }
            return render(
                request=request,
                context=context_dict,
                template_name="templates/profesors.html"
            )

    profile_form = Profile_form(request.POST)
    context_dict = {
        'profile_form': profile_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='templates/profesor_django_fuorms.html'
    )

def update_profile(request, pk: int):
    profile = Profile.objects.get(pk=pk)

    if request.method == 'POST':
        profile_form = Profile_form(request.POST)
        if profile_form.is_valid():
            data = profile_form.cleaned_data
            profile.name = data['name']
            profile.last_name = data['last_name']
            profile.email = data['email']
            profile.artist_name = data['artist_name']
            profile.country = data['country']
            profile.save()

            profiles = Profile.objects.all()
            context_dict = {
                'profiles': profiles

            }
            return render(
                request=request,
                context=context_dict,
                template_name="templates/profiles.html"
            )

    profile_form = Profile_form(model_to_dict(profile))
    context_dict = {
        'profile': profile,
        'profile_form': profile_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='templates/profile_form.html'
    )


def delete_profile(request, pk: int):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        profile.delete()

        profiles = Profile.objects.all()
        context_dict = {
            'profiles': profiles
        }
        return render(
            request=request,
            context=context_dict,
            template_name="templates/profiles.html"
        )

    context_dict = {
        'profile': profiles,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='templates/profile_confirm_delete.html'
    )


def stock_forms_django(request):
    if request.method == 'POST':
        stock_form = Stock_form(request.POST)
        if stock_form.is_valid():
            data = stock_form.cleaned_data
            stock = Stock(
                art_piece=data['art_piece'],
                art_type=data['style'],
                price=data['$'],
                available=data['stock']
            )
            stock.save()

            stock_ = Stock.objects.all()
            context_dict = {
                'stock': stock_
            }
            return render(
                request=request,
                context=context_dict,
                template_name="templates/stock.html"
            )

    stock_form = Stock_form(request.POST)
    context_dict = {
        'stock_form': stock_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='templates/stock_django_forms.html'
    )

'''
def search(request):
    context_dict = dict()
    if request.GET['text_search']:
        search_param = request.GET['text_search']
        courses = Course.objects.filter(name__contains=search_param)
        context_dict = {
            'courses': courses
        }
    elif request.GET['code_search']:
        search_param = request.GET['code_search']
        courses = Course.objects.filter(code__contains=search_param)
        context_dict = {
            'courses': courses
        }
    elif request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(name__contains=search_param)
        query.add(Q(code__contains=search_param), Q.OR)
        courses = Course.objects.filter(query)
        context_dict = {
            'courses': courses
        }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/home.html",
    )

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class CourseListView(ListView):
    model = Course
    template_name = "app_coder/course_list.html"


class CourseDetailView(DetailView):
    model = Course
    template_name = "app_coder/course_detail.html"


class CourseCreateView(CreateView):
    model = Course
    # template_name = "app_coder/course_form.html"
    # success_url = "/app_coder/courses"
    success_url = reverse_lazy('app_coder:course-list')
    fields = ['name', 'code']


class CourseUpdateView(UpdateView):
    model = Course
    # template_name = "app_coder/course_form.html"
    # success_url = "/app_coder/courses"
    success_url = reverse_lazy('app_coder:course-list')
    fields = ['name', 'code']


class CourseDeleteView(DeleteView):
    model = Course
    # success_url = "/app_coder/courses"
    success_url = reverse_lazy('app_coder:course-list') '''
