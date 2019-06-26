import sys
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from liwavespellapplication.services.web.magicseaweed import MSW_WebRequest

from .models import Spot

class HomeView(ListView):
    model = Spot
    template_name = 'liwavespellapplication/home.html'
    context_object_name = 'data'
    paginate_by = 1

    def __init__(self):
        super(HomeView, self)
        self.__data = self.get_msw_context_data()

    #def get_context_data(self, **kwargs):
        #context = super(HomeView, self).get_context_data(**kwargs)
        #context.update({'data': self.spot_selections()})
        #return context

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

            spot_selections_objects = self.spot_selections()
            print(spot_selections_objects)

            return {
                'lb_stats' : longbeach_json_cleaned,
                'rm_stats' : robertmoses_json_cleaned,
                'spots' : spot_selections_objects
            }
        except: 
            context = {'get_msw_context_data()': sys.exc_info()[0]}
            return context
    
    def spot_selections(self):
        try:
            longbeachSpot = {
                'image': 'https://cdn.traveltripper.io/site-assets/192_434_2522/media/2017-04-03-150546/best-views-long-beach-new-york.jpg',
                'name': 'Long Beach',
                'description': 'Long Beach description here...'
            }
            robertmosesSpot = {
                'image': 'https://i.ytimg.com/vi/R1BUE9V5i1w/maxresdefault.jpg',
                'name': 'Robert Moses State Park',
                'description': 'Robert Moses description here...'
            }

            return [
                longbeachSpot,
                robertmosesSpot,
                longbeachSpot,
                robertmosesSpot
            ]
        except:
            context = {'spot_selections()': sys.exc_info()[0]}
            return context





