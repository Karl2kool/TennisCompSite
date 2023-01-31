from asyncio import create_task
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.
from .models import Fillin, Score, Match, Week
from django.views.generic.base import View
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('manager')


class Management(LoginRequiredMixin, TemplateView):
    template_name = "base/manager.html"
    context_object_name = 'manager'

class Home(TemplateView):
    template_name = "base/home.html"
    context_object_name = 'home'

class ReserveList( ListView):
    model = Fillin
    context_object_name = 'reserve'
    template_name = 'base/reserves.html'

class ScoreBoard( ListView):
    model = Score
    context_object_name = 'scoreboard'
    template_name = 'base/scoreboard.html'
  
    def get_queryset(self):
      return Score.objects.all().order_by('total')



class MatchesByWeekView(ListView):
    model = Week
    template_name = 'base/matches.html'
    context_object_name = 'weeks'

class ManageMatches( LoginRequiredMixin, ListView):
    model = Week
    context_object_name = 'weeks'
    template_name = 'base/managematch.html'
 



class ManageReserve(LoginRequiredMixin,  ListView):
    model = Fillin
    context_object_name = 'managereserve'
    template_name = 'base/managereserve.html'

class ReserveUpdate(LoginRequiredMixin, UpdateView):
    model = Fillin
    fields = '__all__'
    success_url = reverse_lazy('manager')
    

class ReserveCreate(LoginRequiredMixin, CreateView):
    model = Fillin
    fields =  '__all__'
    success_url = reverse_lazy('manager')



class ReserveDelete(LoginRequiredMixin, DeleteView):
    model = Fillin
    context_object_name = 'fillin'
    success_url = reverse_lazy('manager')

class ScoreUpdate(LoginRequiredMixin, UpdateView):
    model = Score
    fields = '__all__'
    success_url = reverse_lazy('managescore')

class MatchUpdate(LoginRequiredMixin, UpdateView):
    model = Match
    fields = '__all__'
    success_url = reverse_lazy('managematch')



class ManageScore( LoginRequiredMixin, ListView):
    model = Score
    context_object_name = 'scoreboard'
    template_name = 'base/managescore.html'

    def get_queryset(self):
      return Score.objects.all().order_by('-total')

class ScoreCreate(LoginRequiredMixin, CreateView):
    model = Score
    fields =  '__all__'
    success_url = reverse_lazy('managescore')

class MatchCreate(LoginRequiredMixin, CreateView):
    model = Match
    fields =  '__all__'
    success_url = reverse_lazy('managematch')








  
