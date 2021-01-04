

from django.urls import path
from . import views
urlpatterns = [
    path('', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('signup', views.signup, name='signup'),
    path('news', views.news, name='news'),
    path('home', views.home, name='home'),
    path('share', views.share, name='share'),

    path('myCollection', views.myCollection, name='myCollection'),
    path('newsBee', views.newsBee, name='newsBee'),




    #path('signin', views.Signin.as_view() ,name='signin'),

]
