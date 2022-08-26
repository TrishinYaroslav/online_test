from django.urls import path
from toster.views import index, test3

urlpatterns = [
    path('', index, name='index'),
    path('test3', test3, name='test3'),
]
