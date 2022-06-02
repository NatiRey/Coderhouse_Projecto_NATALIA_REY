from django.shortcuts import render
from django.db.models import Q
from django.forms.models import model_to_dict

from ARTYapp.models import Profile, Project, Stock, Atelier
from ARTYapp.forms import Profile_form, Project_form, Stock_form, Atelier_form


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


def atelier_(request):
    atelier_ = Atelier.objects.all()

    context_dict = {
        'atelier_': atelier_
    }

    return render(
        request=request,
        context=context_dict,
        template_name="templates/atelier_.html")

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
        template_name="templates/stocks.html")

def form_hmtl(request):

    if request.method == 'POST':
        atelier = Project(name=request.POST['atelier'], code=request.POST['adress'])
        atelier.save()

        atelier_ = Atelier.objects.all()
        context_dict = {
            'atelier': atelier_
        }

        return render(
            request=request,
            context=context_dict,
            template_name="templates/atelier_.html"
        )

    return render(
        request=request,
        template_name='templates/formHTML.html'
    )


def atelier_forms_django(request):
    if request.method == 'POST':
        atelier_form = Atelier_form(request.POST)
        if atelier_form.is_valid():
            data = atelier_form.cleaned_data
            atelier = Atelier(name=data['atelier'], adress=data['adress'])
            atelier.save()

            atelier_ = Atelier.objects.all()
            context_dict = {
                'atelier_': atelier_
           }
            return render(
                request=request,
                context=context_dict,
                template_name="templates/atelier_.html"
            )

    atelier_form = Atelier_form(request.POST)
    context_dict = {
       'atelier_form': atelier_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='templates/atelier_django_forms.html'
    )


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

def search(request):
    context_dict = dict()
    if request.GET['text_search']:
        search_param = request.GET['text_search']
        atelier_ =  Atelier.objects.filter(name__contains=search_param)
        context_dict = {
            'atelier_': atelier_
        }
    elif request.GET['atelier_search']:
        search_param = request.GET['atelier_search']
        atelier_ = Atelier.objects.filter(code__contains=search_param)
        context_dict = {
            'atelier_': atelier_
        }
    elif request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(name__contains=search_param)
        query.add(Q(code__contains=search_param), Q.OR)
        atelier_ = Atelier.objects.filter(query)
        context_dict = {
            'atelier_': atelier_
        }

    return render(
        request=request,
        context=context_dict,
        template_name="templates/home.html",
    )

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class AtelierListView(ListView):
    model = Atelier
    template_name = "templates/atelier-list.html"


class AtelierDetailView(DetailView):
    model = Atelier
    template_name = "templates/atelier_detail.html"


class AtelierCreateView(CreateView):
    model = Atelier
    #template_name = "templates/atelier_form.html"
    #success_url = "templates/atelier_"
    success_url = reverse_lazy('templates:atelier-list')
    fields = ['atelier', 'adress']


class AtelierUpdateView(UpdateView):
    model = Atelier
    # template_name = "templates/atelier_form.html"
    # success_url = "templates/atelier_"
    success_url = reverse_lazy('templates:atelier-list')
    fields = ['atelier', 'adress']


class AtelierDeleteView(DeleteView):
    model = Atelier
    # success_url = "/ARTYapp/atelier_"
    success_url = reverse_lazy('templates:atelier-list')
