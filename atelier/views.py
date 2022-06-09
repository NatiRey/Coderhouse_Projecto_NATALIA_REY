
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from atelier.models import Atelier

class AtelierListView(ListView):
    model = Atelier
    template_name = "atelier/atelier_list.html"


class AtelierDetailView(DetailView):
    model = Atelier
    template_name = "atelier/atelier_detail.html"
    fields = ['atelier', 'adress', 'description']


class AtelierCreateView(LoginRequiredMixin, CreateView):
    model = Atelier
    success_url = reverse_lazy('atelier:atelier-list')
    fields = ['atelier', 'adress', 'description']


class AtelierUpdateView(LoginRequiredMixin, UpdateView):
    model = Atelier
    success_url = reverse_lazy('atelier:atelier-list')
    fields = ['atelier', 'adress', 'description']


class AtelierDeleteView(LoginRequiredMixin, DeleteView):
    model = Atelier
    success_url = reverse_lazy('atelier:atelier-list')
