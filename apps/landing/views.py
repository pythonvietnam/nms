from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import CreateView
from apps.landing.models import Landing
from apps.base.views import (BaseView, LoginRequiredMixin)

# Create your views here.

class LandingView(BaseView, CreateView):
    """docstring for LandingView"""
    model = Landing
    fields = ['email']
    template_name = 'landing/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info = {
            'info': {
                'title': 'NMS',
            },
        }
        context.update(info)
        return context

    def form_valid(self, form):
        form.save()
        return HttpResponse('Email sent')

    def form_invalid(self, form):
        return HttpResponse("Email has been send!")


