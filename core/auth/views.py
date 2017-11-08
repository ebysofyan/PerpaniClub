from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from core.orm.models import Club, Member, City

# Create your views here.


class LoginView(View):
    template_name = 'base/login.html'

    def get(self, request):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/club/')

        city_labels = [city.name for city in City.objects.all()]
        city_values = [city.clubs.count() for city in City.objects.all()]

        club_member_labels = [club.name for club in Club.objects.all()]
        club_member_values = [club.members.count()
                              for club in Club.objects.all()]

        data = {
            'club': {
                'total': Club.objects.all().count(),
                'labels': club_member_labels,
                'member_count': club_member_values,
            },
            'member': {
                'total': Member.objects.all().count(),
                'coach_total': Member.objects.filter(position='Coach').count()
            },
            'citys': {
                'labels': city_labels,
                'values': city_values,
            }
        }
        return render(request, self.template_name, data)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('/club/')

        else:
            messages.add_message(request, messages.WARNING,
                                 'Username dan atau Password tidak ditemukan')
        return self.get(request)


class LogoutView(View):

    def get(self, request):
        if request.user:
            logout(request)
            return HttpResponseRedirect('/')

        return HttpResponseRedirect('/')


class ErrorView(TemplateView):
    template_name = 'base/error.html'
