from django.db import IntegrityError
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (CreateView, ListView, DeleteView)
from django.http import HttpResponse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from apps.ip.models import IP
from apps.base.views import (BaseView, LoginRequiredMixin)
from .utils import UtilsIP
import json


class IPAPIList(BaseView):
    def get(self, request, *args, **kwargs):
        util_ip = UtilsIP()
        result = util_ip.get_list_ip('')
        return HttpResponse(json.dumps(result))


class APIIPCreateView(BaseView):
    def post(self, request, *args, **kwargs):
        pass


class IPListView(BaseView, LoginRequiredMixin, ListView):
    """docstring for IPListView"""
    model = IP
    template_name = 'ip/index.html'

    def get_queryset(self):
        return IP.objects.filter(user_profile=self.request.user.profile).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'List Address - NMS',
            },
        }
        context.update(info)
        return context


class IPCreateView(BaseView, LoginRequiredMixin, CreateView):
    """docstring for IPCreateView"""
    model = IP
    fields = ['address', 'vhost']
    template_name = 'ip/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'New IP Address - NMS',
            },
        }
        context.update(info)
        return context

    def form_valid(self, form):
        # Save IP
        
        try:
            ip = form.save(commit=False)

            if self.validateEmail(ip.address):
                form._errors['address'] = form.error_class(['Please dont use your email. '
                                                       'Please supply a different ip address.'])
                return super().form_invalid(form)

            if self.request.user.profile.subscription == 1 and ip.vhost:
                return super().form_invalid(form)
            ip.user_profile = self.request.user.profile
            ip.save()
        except IntegrityError:
            form._errors['address'] = form.error_class(['This address is already in use. '
                                                           'Please supply a different ip address.'])
            return super().form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ip')

    def validateEmail(self, email):
        try:
            if email and 'http' in email:
                email = email.split('://')[1].lower()
                if '/' in email:
                    email = email.split('/')[0]
            validate_email(email)
            return True
        except ValidationError:
            return False


class IPDeleteView(BaseView, LoginRequiredMixin, DeleteView):
    """docstring for IPDeleteView"""
    model = IP

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user_profile == self.request.user.profile:
            return self.post(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get_success_url(self):
        return reverse_lazy('ip')



