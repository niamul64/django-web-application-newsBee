from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.generic import ListView,detail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import authenticate, login

from .forms import UserReg, ExtentUser
from .models import ExtentionUser, Share
import http.client, urllib.parse # mediastack
import requests
import json
# Create your views here.

def signin(request):
    if request.method == 'POST':
        user =auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        print (request.POST['username'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin.html',{'error':"incorrect user name or password"})

    return render(request, 'signin.html')
def signout(request):
    if request.method == 'POST':
        auth.logout(request)

    return redirect('signin')


def signup(request):
    if request.user.is_authenticated:
        print ("loged in")
        return redirect('home')

    e=''
    if request.method == 'POST':
        form1 = UserReg(request.POST)
        form2 = ExtentUser(request.POST)

        if form1.is_valid() and form2.is_valid() and len(form1.cleaned_data['email'])>9 :
            userSaved=form1.save()


            ExtentionUser(author =userSaved, fullName=form2.cleaned_data['fullName'], country= form2.cleaned_data['country']).save()
            return redirect('signin')

        elif len(form1.cleaned_data['password1'])<8 :
            return render(request, 'signup.html', {'error': "password didn't matched or too short",'form1':form1,'form2':form2})
        else:
            return render(request, 'signup.html',{'error': "fill the form correctly", 'form1': form1, 'form2': form2})
    form1=UserReg()
    form2=ExtentUser()
    return render(request, 'signup.html', {'error':e , 'form1':form1,'form2':form2})



def news(request):

    details = get_object_or_404(ExtentionUser, author=request.user.id)
    country = details.country



    conn = http.client.HTTPConnection('api.mediastack.com')

    params = urllib.parse.urlencode({
        'access_key': '325490ab1e265963d046fa76ec53fe98',
        'limit': 10,
        'sort': 'published_desc',
        'countries': country,
        'languages': 'en',
    })

    conn.request('GET', '/v1/news?{}'.format(params))

    res = conn.getresponse()
    data = res.read()
    absData  = json.loads(data)
    allData = absData['data']

    if request.method == 'GET' and  request.GET.get('search')!=None:
        se = request.GET.get('search')

        select=[]
        for i in allData:

            try:
                d = i["published_at"].split('T')
                i["published_at"] = d[0]
                if se in i["title"]:
                    select.append(i)
            except:
                pass
        return render(request, 'news.html', {'data': select})
    for i in allData:
        try:
            d=  i["published_at"].split('T')
            i["published_at"]=d[0]
        except:
            pass
    return render(request, 'news.html', {'data': allData})


def home(request):

    conn = http.client.HTTPConnection('api.mediastack.com')

    params = urllib.parse.urlencode({
        'access_key': '325490ab1e265963d046fa76ec53fe98',

        'sort': 'published_desc',
        'limit': 10,
        'languages': 'en',

    })

    conn.request('GET', '/v1/news?{}'.format(params))

    res = conn.getresponse()
    data = res.read()
    absData  = json.loads(data)
    allData = absData['data']


    if request.method == 'GET' and  request.GET.get('search')!=None:
        se = request.GET.get('search')

        select=[]
        for i in allData:

            try:
                d = i["published_at"].split('T')
                i["published_at"] = d[0]

                if se in i["title"]:
                    select.append(i)

            except:
                pass
        return render(request, 'home.html', {'data': select})
    for i in allData:

        try:
            d=i["published_at"].split('T')
            i["published_at"]=d[0]
        except:
            pass



    return render(request, 'home.html', {'data':allData})




def share(request):
    if request.method == 'POST':
        img = request.POST['img']
        title = request.POST['title']
        auth = request.POST['author']

        des = request.POST['des']

        cat = request.POST['cat']

        date = request.POST['date']

        url = request.POST['url']

        country = request.POST['country']


    return render(request, 'share.html', {'img':img, 'title':title, 'author':auth, 'des':des, 'cat':cat,'date':date,'url':url, 'country':country  })

def myCollection(request):
    msg=''
    if request.method == 'POST':
        comment = request.POST['comment']

        img = request.POST['img']

        title= request.POST['title']

        auth = request.POST['author']


        des= request.POST['des']


        cat = request.POST['cat']

        date= request.POST['date']

        url=request.POST['url']

        country =request.POST['country']

        Share(author= request.user, newsAuthor=auth , comment=comment , country=country, url=url, img=img, newsDate=date, category=cat, description=des, title=title ).save()
        msg='A news is collected'
#

    collection = Share.objects.all().filter(author=request.user).order_by("-share_date")

    if not collection:
        msg="You don't have any shared news"


    return render(request, 'myCollection.html', {'data': collection, 'msg':msg  })



def newsBee(request):
    details = get_object_or_404(ExtentionUser, author=request.user.id)
    userCountry = details.country

    collection = Share.objects.all().order_by("-share_date")



    return render(request, 'newsBee.html', {'data': collection})

class delete(DeleteView):
    model=Share
    template_name='delete.html'
    success_url = 'myCollection/'