from django.urls import path
#we import all the views we created here
#to set up the urls
from AppTwo import views


urlpatterns = [
    path('', views.users, name='users')
]
