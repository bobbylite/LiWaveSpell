import sys
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from liwavespellapplication.services.web.magicseaweed import MSW_WebRequest

from .models import Spot

class HomeViewDark(ListView):
    model = Spot
    template_name = 'liwavespellapplication/home.html'
    context_object_name = 'spots'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super(HomeViewDark, self).get_context_data(**kwargs)
        context.update({'theme': {
            'navbg': 'dark',
            'navtext': 'light',
            'bodybg': 'secondary',
            'cardbg': 'dark',
            'cardtext': 'light',
        }})
        return context

class HomeViewLight(ListView):
    model = Spot
    template_name = 'liwavespellapplication/home.html'
    context_object_name = 'spots'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super(HomeViewLight, self).get_context_data(**kwargs)
        context.update({'theme': {
            'navbg': 'primary',
            'navtext': 'dark',
            'bodybg': 'light',
            'cardbg': 'light',
            'cardtext': 'dark',
        }})
        return context


class DetailView(DetailView):

    template_name = 'liwavespellapplication/home.html'
    context_object_name = 'data'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context.update({'data': self.spot_selections()})
        return context

    def get_msw_context_data(self):
        try: 

            msw_longbeach_request = MSW_WebRequest("http://magicseaweed.com/api/{}/forecast/?spot_id=383")
            msw_robertmoses_request = MSW_WebRequest("http://magicseaweed.com/api/{}/forecast/?spot_id=381")

            longbeach_data = msw_longbeach_request.get()
            longbeach_json = MSW_WebRequest.parse(longbeach_data)

            robertmoses_data = msw_robertmoses_request.get()
            robertmoses_json = MSW_WebRequest.parse(robertmoses_data)

            longbeach_json_cleaned = MSW_WebRequest.Clean_Datetime(longbeach_json)
            robertmoses_json_cleaned = MSW_WebRequest.Clean_Datetime(robertmoses_json)

            context = {
                'lb_stats' : longbeach_json_cleaned,
                'rm_stats' : robertmoses_json_cleaned
            }

            null_or_empty = None == context

            return {'get_msw_context_data()': 'NullOrEmpty'} if null_or_empty else context

        except: 
            context = {'get_msw_context_data()': sys.exc_info()[0]}
            return context






