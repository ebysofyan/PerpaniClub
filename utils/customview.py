from django.views.generic import (
    View,
    ListView,
    DetailView,
    UpdateView,
    TemplateView,
    CreateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test


class UserStaffMixin(object):

    @method_decorator(user_passes_test(lambda u: u.is_staff, login_url='/error/'))
    def dispatch(self, request, *args, **kwargs):
        return super(UserStaffMixin, self).dispatch(request, *args, **kwargs)


class LoginRequiredGenericView(LoginRequiredMixin, UserStaffMixin, View):
    login_url = '/error/'


class LoginRequiredTemplateView(LoginRequiredMixin, UserStaffMixin, TemplateView):
    login_url = '/error/'


class LoginRequiredListView(LoginRequiredMixin, UserStaffMixin, ListView):
    login_url = '/error/'


class LoginRequiredDetailView(LoginRequiredMixin, UserStaffMixin, DetailView):
    login_url = '/error/'


class LoginRequiredCreateView(LoginRequiredMixin, UserStaffMixin, CreateView):
    login_url = '/error/'


class LoginRequiredUpdateView(LoginRequiredMixin, UserStaffMixin, UpdateView):
    login_url = '/error/'
