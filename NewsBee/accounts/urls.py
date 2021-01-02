

from django.urls import path
from . import views
urlpatterns = [
    path('', views.signin ,name='signin'),
    path('signout', views.signout ,name='signout'),
    path('/signup', views.signup ,name='signup'),


    #path('signin', views.Signin.as_view() ,name='signin'),

]
