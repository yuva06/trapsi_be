from django.urls import path
from django.conf.urls import url 
from .views import *

urlpatterns=[
    path("Blog/",BlogListView.as_view()),
    path("Blog/<pk>",BlogDetialView.as_view()),

    path("RegistrationApplication/",RegistrationApplicationListView.as_view()),
    path("RegistrationApplication/<pk>",RegistrationApplicationDetialView.as_view()),

    path("Enquire/",EnquireListView.as_view()),
    path("Enquire/<pk>",EnquireDetialView.as_view()),

    path("Client/",ClientListView.as_view()),
    path("Client/<pk>",ClientDetialView.as_view()),
    
    path("ClientForm/",ClientFormListView.as_view()),
    path("ClientForm/<pk>",ClientFormDetialView.as_view()),

]