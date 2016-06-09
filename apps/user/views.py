from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout

from apps.landing.models import Landing
from apps.base.views import (BaseView, LoginRequiredMixin)


class UserProfileView(BaseView, LoginRequiredMixin, TemplateView):
    """docstring for AboutView"""
    template_name = 'user/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'User Profile - NMS',
            },
        }
        context.update(info)
        return context