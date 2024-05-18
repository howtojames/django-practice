from django.shortcuts import render
#added
from django.http import HttpResponse
#conect view to database
from first_app.models import Topic, Webpage, AccessRecord
# Create your views here.

#this is one view called index
#each view is a function in the views.py (this file)
#each view must return a HttpResponse object
#HttpResponse is takes in a string of the content
def index(request):
    #this is querying, returns a list of objects
    webpages_list = AccessRecord.objects.order_by('date')
    #we use access_records in index.html
    date_dict = {'access_records':webpages_list}
    #my_dict = {'insert_me':"Hello I am from first_app/index.html"}
    return render(request, 'first_app/index.html', context=date_dict)
