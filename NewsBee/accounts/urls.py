

from django.urls import path
from . import views
urlpatterns = [
    path('', views.signin ,name='signin'),

    #path('signin', views.Signin.as_view() ,name='signin'),

]
