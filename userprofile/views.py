# coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from schedule.models import Enrolled, ClassEnrolled, TallerGuitarra, Observador, Inter, Intensivo, Elemental,\
    Independiente
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .forms import CompleteProfile
from core.models import UserProfileInfo


def index(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            user = request.user()
            talleres_guitarra = TallerGuitarra.objects.all()
            observadores = Observador.objects.all()
            interdisciplinario = Inter.objects.all()
            intensivo = Intensivo.objects.all()
            elemental = Elemental.objects.all()
            independiente = Independiente.objects.all()
            context = {
                'elemental': elemental,
                'intensivo': intensivo,
                'interdisciplinario': interdisciplinario,
                'talleres_guitarra': talleres_guitarra,
                'observadores': observadores,
                'independiente': independiente,
            }
            return render(request, 'userprofile/admin.html', context)
        user = request.user
        try:
            enrolled = Enrolled.objects.get(user=user)
        except Enrolled.DoesNotExist:
            enrolled = None
        if enrolled is not None:
            talleres_guitarra = TallerGuitarra.objects.filter(id_enrolled=user)
            observadores = Observador.objects.filter(id_enrolled=user)
            interdisciplinario = Inter.objects.filter(id_enrolled=user)
            intensivo = Intensivo.objects.filter(id_enrolled=user)
            elemental = Elemental.objects.filter(id_enrolled=user)
            independiente = Independiente.objects.filter(id_enrolled=user)
            context = {
                'elemental': elemental,
                'intensivo': intensivo,
                'interdisciplinario': interdisciplinario,
                'talleres_guitarra': talleres_guitarra,
                'enrolled': enrolled,
                'observadores': observadores,
                'independiente': independiente,
            }
            return render(request, 'userprofile/profile.html', context)
    return render(request, 'userprofile/profile.html')


def profile(request):
    if request.user.is_authenticated:
        user = request.user
        #Case logged user with enrolled form completed
        try:
            enrolled = Enrolled.objects.get(user=user)
        except Enrolled.DoesNotExist:
            enrolled = None
        if enrolled is not None:
            context = {
                'enrolled': enrolled,
            }
            return render(request, 'schedule/already_enrolled.html', context)

        #Case logged user completing enrolled form
        if request.method == 'POST':
            form = CompleteProfile(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user
                if (obj.academy and not obj.academy_country) or (not obj.academy and obj.academy_country):
                    error = "Por favor especifica todos los datos de la institución. Déjalos en blanco si no aplica"
                    return render(request, 'schedule/enrolled_form.html', {'error': error, 'form': form})
                obj.save()
                return HttpResponseRedirect(reverse_lazy('userprofile'))
            error = "Por favor completa todos los campos obligatorios"
            return render(request, 'schedule/enrolled_form.html', {'error': error, 'form': form})

        #Case logged user but enrolled form has not been completed
        form = CompleteProfile()
        return render(request, 'schedule/enrolled_form.html', {'form': form})

    #Case not logged
    return render(request, 'schedule/enrolled_form.html')
