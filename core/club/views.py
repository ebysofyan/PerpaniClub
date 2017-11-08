from django.shortcuts import render
from utils.customview import (
    LoginRequiredGenericView,
    LoginRequiredListView,
    LoginRequiredDetailView,
    LoginRequiredUpdateView,
    LoginRequiredTemplateView,
    LoginRequiredCreateView
)
from utils.datediff import get_age_category
from django.http import HttpResponse
from .forms import ClubForm
from core.orm.models import City, Member

# Create your views here.


class ClubDetailView(LoginRequiredTemplateView):
    template_name = 'core/club/club_detail.html'

    def get(self, request):
        age_category_list = [get_age_category(
            x[0]) for x in Member.objects.all().values_list('born_date')]
        club = request.user.member.club
        data = {
            'menu': 'club',
            'subtitle': 'Detail Klub',
            'member': {
                'total': club.members.all().count(),
                'coach_total': club.members.all().filter(position='Coach').count(),
                'male_total': club.members.filter(gender='pria').count(),
                'female_total': club.members.filter(gender='wanita').count(),
                'anak': len([x for x in age_category_list if x == 'Anak']),
                'remaja': len([x for x in age_category_list if x == 'Remaja']),
                'dewasa': len([x for x in age_category_list if x == 'Dewasa']),
            }
        }
        return render(request, self.template_name, data)


class ClubEditView(LoginRequiredUpdateView):
    template_name = 'core/club/club_edit.html'
    form_class = ClubForm
    success_url = '/club/'

    def get(self, request):
        data = {
            'menu': 'club',
            'subtitle': 'Ubah Informasi Klub',
            'citys': City.objects.all()
        }
        return render(request, self.template_name, data)

    def get_object(self):
        return self.request.user.member.club

    def form_valid(self, form):
        self.object = form.save()
        return super(ClubEditView, self).form_valid(form)
