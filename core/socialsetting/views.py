from django.shortcuts import render, redirect
from utils.customview import (
    LoginRequiredGenericView,
    LoginRequiredCreateView,
    LoginRequiredUpdateView,
)
from core.orm.models import SocialAccount
from .forms import SocialAccountForm
# Create your views here.


class SocialSettingView(LoginRequiredCreateView):
    template_name = 'core/socialsetting/social_setting.html'
    form_class = SocialAccountForm

    def get(self, request):
        data = {
            'menu': 'setting',
            'subtitle': 'Tambah',
            'social_list': SocialAccount.objects.all()
        }

        return render(request, self.template_name, data)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.club = self.request.user.member.club
        obj.save()

        return redirect('setting:view')

    def form_invalid(self):
        return self.get(request)


class SocialSettingEditView(LoginRequiredUpdateView):
    template_name = 'core/socialsetting/social_setting_edit.html'
    form_class = SocialAccountForm

    def get(self, request, **kwargs):
        data = {
            'menu': 'setting',
            'subtitle': 'Tambah',
            'object': self.get_object,
            'social_list': SocialAccount.objects.all()
        }

        return render(request, self.template_name, data)

    def get_object(self):
        return SocialAccount.objects.get(pk=self.kwargs.get('pk'))

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()

        return redirect('setting:view')

    def form_invalid(self):
        return self.get(request)


class SocialSettingDeleteView(LoginRequiredGenericView):

    def get(self, request, pk):
        object = SocialAccount.objects.get(pk=pk)
        if object:
            object.delete()
            return redirect('setting:view')
