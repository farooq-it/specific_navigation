from app2.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('two1/',two1,name='two1'),
    path('two2/',two2,name='two2'),
]