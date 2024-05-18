import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()
#list
topics = ['Search', 'Social', 'MarketPlace', 'News', 'Games']


def add_topic():
    #retrieve or create it
    #get_or_create reuturns a tuple, first returns a reference to the model instance
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t  #returns an saved Topic object


def populate(N=5):
    for entry in range(N):
        top = add_topic() #this is an saved Topic object

        fake_url= fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        #passign in webpage here
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

#checks if the script is being executed directly (not imported)
if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")
