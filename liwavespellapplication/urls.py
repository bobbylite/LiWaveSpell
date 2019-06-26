from django.urls import path
from liwavespellapplication.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='liwavespell-home'),
    path('<str:theme>/', HomeView.as_view(), name='liwavespell-home-theme'),
]