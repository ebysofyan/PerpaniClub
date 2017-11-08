from django.shortcuts import render, redirect
from utils.customview import (
    LoginRequiredGenericView,
    LoginRequiredListView,
    LoginRequiredDetailView,
    LoginRequiredUpdateView,
    LoginRequiredTemplateView,
    LoginRequiredCreateView
)
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from core.orm.models import Member
from django.contrib.auth.models import User
from .forms import MemberForm
from django.db.models import Q
from django.contrib import messages

# Create your views here.


class MemberListView(LoginRequiredListView):
    template_name = 'core/member/member_list.html'
    model = Member
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        if q:
            messages.add_message(self.request, messages.INFO, q)
            return Member.objects.filter(Q(club=self.request.user.member.club) &
                                         Q(name__contains=q) |
                                         Q(gender__contains=q) |
                                         Q(user__username__contains=q))

        return Member.objects.filter(club=self.request.user.member.club)

    def get_context_data(self, **kwargs):
        context = super(MemberListView, self).get_context_data(**kwargs)
        context['menu'] = 'member'
        context['subtitle'] = 'Semua Anggota'
        return context


class MemberDetailView(LoginRequiredTemplateView):
    template_name = 'core/member/member_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MemberDetailView, self).get_context_data(**kwargs)
        context['menu'] = 'member'
        context['subtitle'] = 'Detail Anggota'
        context['member'] = Member.objects.get(
            club=self.request.user.member.club, pk=kwargs.get('pk'))

        return context


class MemberAddView(LoginRequiredCreateView):
    template_name = 'core/member/member_add.html'
    form_class = MemberForm
    success_url = '/member/'

    def get(self, request, **kwargs):
        data = {
            'menu': 'member',
            'subtitle': 'Tambah Anggota Baru'
        }
        return render(request, self.template_name, data)

    def form_valid(self, form):
        obj = form.save(commit=False)

        user = User()
        user.username = self.request.POST['username']
        user.set_password(self.request.POST['password'])
        if not self.request.POST.get('staff', None) == None:
            user.is_staff = True
        user.save()

        obj.user = user
        obj.club = self.request.user.member.club
        obj.save()

        return HttpResponseRedirect(reverse_lazy('member:detail', kwargs={'pk': obj.id}))


class MemberEditView(LoginRequiredUpdateView):
    template_name = 'core/member/member_edit.html'
    form_class = MemberForm
    success_url = '/member/'

    def get(self, request, **kwargs):
        data = {
            'menu': 'member',
            'subtitle': 'Ubah Informasi Anggota',
            'member': self.get_object()
        }

        return render(request, self.template_name, data)

    def get_object(self):
        return Member.objects.get(club=self.request.user.member.club, pk=self.kwargs.get('pk'))

    def form_valid(self, form):
        obj = form.save(commit=False)
        user = self.object.user
        user.username = self.request.POST.get('username')
        if not self.request.POST.get('passwd_change', 'off') == 'off':
            user.set_password(request.POST['password'])

        if not self.request.POST.get('staff', None) == None:
            user.is_staff = True

        user.save()
        obj.save()

        return HttpResponseRedirect(reverse_lazy('member:detail', kwargs={'pk': self.object.id}))


class MemberDeleteView(LoginRequiredGenericView):

    def get(self, request, **kwargs):
        member = Member.objects.get(pk=kwargs.get('pk'))
        if member:
            member.delete()

            return redirect('member:view')
