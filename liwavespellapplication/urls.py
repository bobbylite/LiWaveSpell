from django.urls import path
from liwavespellapplication.views import HomeViewDark, HomeViewLight

urlpatterns = [
    path('/dark/', HomeViewDark.as_view(), name='liwavespell-home-dark'),
    path('/light/', HomeViewLight.as_view(), name='liwavespell-home-light'),
]