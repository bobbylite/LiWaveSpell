import sys
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from liwavespellapplication.services.web.magicseaweed import MSW_WebRequest

from .models import Spot

class HomeView(ListView):
    model = Spot
    template_name = 'liwavespellapplication/home.html'
    context_object_name = 'spots'
    paginate_by = 1

    __dark_theme = {'theme': {
        'skin': 'dark',
        'navbg': 'dark',
        'navtext': 'light',
        'bodybg': 'secondary',
        'cardbg': 'dark',
        'cardtext': 'light',
        'dropdowntext': 'secondary',
        'footerbg': 'dark'
    }}

    __light_theme = {'theme': {
        'skin': 'light',
        'navbg': 'primary',
        'navtext': 'dark',
        'bodybg': 'light',
        'cardbg': 'light',
        'cardtext': 'dark',
        'dropdowntext': 'light',
        'footerbg': 'primary'
    }}

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        params = self.kwargs
               
        if params != {}:
            if params['theme'] != None:
                theme = self.__dark_theme if params['theme'] == 'dark' else self.__light_theme
        else:
            theme = self.__light_theme

        context.update(theme)
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






