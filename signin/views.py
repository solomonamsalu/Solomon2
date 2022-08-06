from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup
def say_hello(request):
    signin =Meetup.objects.all()
    return render(request,'index.html',{
        'signin':signin
    })
def detail_meetup(request,meetup_slug):
    print(meetup_slug)
    try:
        selected_meetup =Meetup.objects.get(slug=meetup_slug)
        return render(request,'meetupd.html',{
            'meetup_found':False,
            'meetup_title':selected_meetup.title,
            'meetup_description':selected_meetup.description
        }) 
    except Exception as exc:
        return render(request,'meetupd.html',{
            'meetup_found':True
        })       


