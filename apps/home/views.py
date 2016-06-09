from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout

from apps.landing.models import Landing
from apps.base.views import (BaseView, LoginRequiredMixin)


# Create your views here.
class LoginView(BaseView, TemplateView):
    """docstring for LoginView"""
    template_name = 'home/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Login Page - NMS',
            },
        }
        context.update(info)
        return context


class LogoutView(BaseView):
    """docstring for LogoutView"""
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('home'))


class HomeView(BaseView, LoginRequiredMixin, TemplateView):
    """docstring for HomeView"""
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Home Page - NMS',
            },
        }
        context.update(info)
        return context


class HistoryView(BaseView, LoginRequiredMixin, TemplateView):
    """docstring for HistoryView"""
    template_name = 'home/history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'History Page - NMS',
            },
        }
        context.update(info)
        return context


class AboutView(BaseView, TemplateView):
    """docstring for AboutView"""
    template_name = 'home/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'About Page - NMS',
            },
        }
        context.update(info)
        return context


class HelpView(BaseView, TemplateView):
    """docstring for HelperView"""
    template_name = 'home/help.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'Help Page - NMS',
            },
        }
        context.update(info)
        return context
