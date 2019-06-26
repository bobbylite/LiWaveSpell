from django.urls import path
from liwavespellapplication.views import HomeView

urlpatterns = [
    path('/theme/', HomeView.as_view(), name='liwavespell-home'),
    path('/theme/<str:theme>', HomeView.as_view(), name='liwavespell-home-theme'),
]