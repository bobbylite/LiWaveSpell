from django.shortcuts import render
from django.http import HttpResponse

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
    context = {
        'tweets': tweets
    }
    return render(requet, 'liwavespellapplication/home.html', context)


