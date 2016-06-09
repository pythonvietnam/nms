from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.gzip import gzip_page
from django.http import HttpResponse
from django.views.generic import View
import json

class LoginRequiredMixin(View):
    """docstring for LoginRequiredMixin"""
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class BaseView(View):
    """docstring for BaseView"""
    @method_decorator(gzip_page)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
