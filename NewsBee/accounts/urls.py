

from django.urls import path
from . import views
urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('', views.signup, name='signup'),
    path('news', views.news, name='news'),
    path('home', views.home, name='home'),
    path('share', views.share, name='share'),

    path('myCollection', views.myCollection, name='myCollection'),
    path('delete/myCollection/', views.myCollection, name='delete/myCollection'),
    path('newsBee', views.newsBee, name='newsBee'),
    path('delete/<int:pk>',views.delete.as_view(), name='delete'),




    #path('signin', views.Signin.as_view() ,name='signin'),

]
