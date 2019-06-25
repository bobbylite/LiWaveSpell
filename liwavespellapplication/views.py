from django.shortcuts import render
from django.http import HttpResponse
from liwavespellapplication.services.web.magicseaweed import MSW_WebRequest

tweets = [
    {
        'avatar' : 'img',
        'username' : 'username',
        'time' : 'time',
        'body' : 'tweet body'
    },
    {
        'avatar' : 'img2',
        'username' : 'username2',
        'time' : 'time2',
        'body' : 'tweet2 body'
    }
]

def home(requet):

    msw_longbeach = MSW_WebRequest("http://magicseaweed.com/api/{}/forecast/?spot_id=383")
    msw_robertmoses = MSW_WebRequest("http://magicseaweed.com/api/{}/forecast/?spot_id=381")

    context = {
        'lb_stats' : MSW_WebRequest.parse_JSON(msw_longbeach.get()),
        'rm_stats' : MSW_WebRequest.parse_JSON(msw_longbeach.get())
    }

    return render(requet, 'liwavespellapplication/home.html', context)


