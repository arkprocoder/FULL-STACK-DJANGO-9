from django.urls import path
from icoderapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.handlesignup,name='handlesignup'),
    path('login',views.handlelogin,name='handlelogin'),
    path('logout',views.handlelogout,name='handlelogout'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('blog',views.blog,name='blog'),
    path('portfolio',views.portfolio,name='portfolio'),
    
]
