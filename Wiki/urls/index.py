from django.urls import path, include

from Wiki.views.index import index, signup, signin
from Wiki.views.index import start, stl, basic, advanced

urlpatterns = [
     path("", index, name="index"),
     path('signup', signup, name='signup'),
     path('signin', signin, name='signin'),
     path('start', start, name='start'),
     path('stl', stl, name='stl'),
     path('basic', basic, name='basic'),
     path('advanced', advanced, name='advanced'),
]