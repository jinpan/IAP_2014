"""
This script downloads pages from the externship postings page
"""

from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from IAP_2014.models import Externship


start, end = 4841, 5301
base_loc = '/home/jin/Projects/IAP_2014/pages/%d.html'


def load(num):
    with open(base_loc % num) as f:
        return f.read()

def format(string):
    return string.lower().replace(' ', '_').replace('\'', '')

def parse(num):
    print 'started', num
    soup = BeautifulSoup(load(num))

    data = {'id': num,
            'category': '',
            'title': '',
            'description': '',
            'stipend': '',
            'dates': '',
            'number_of_externs': '',
            'extern_level_preference': '',
            'extern_course_preference': '',
            'requirements': '',
            'name': '',
            'web_address': '',
            'sponsors_job_title': '',
            'externship_location': '',}
    
    try:
        tables = soup.findAll('table')
        for table in tables:
            for row in table.findAll('tr'):
                key, val = row.find('th').text, row.find('td').text
                data[format(key)] = val

        import ipdb; ipdb.set_trace()
        externship = Externship(**data)
        externship.save()

        print 'finished', num
    except:
        print 'failed', num
    


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for idx in range(start, end + 1):
            parse(idx)
