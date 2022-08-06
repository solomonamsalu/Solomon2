from django.urls import path
from . import views
urlpatterns = [
    path('hello/',views.say_hello,name="all_meetups"),
    path('meetups/<slug:meetup_slug>',views.detail_meetup,name="detail_meetup"),

]