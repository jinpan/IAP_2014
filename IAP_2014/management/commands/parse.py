"""
This script downloads pages from the externship postings page
"""

import re
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from IAP_2014.models import Externship


start, end = 4841, 5358
base_loc = 'listings/%d.html'


def load(num):
    with open(base_loc % num) as f:
        return f.read()

def format(string):
    return string.lower().replace(' ', '_').replace('\'', '')

def parse(num):
    #rint 'started', num
    try:
        soup = BeautifulSoup(load(num))
    except:
        #print 'skipping', num
        return

    data = {'id': num,
            'category': '',
            'title': '',
            'description': '',
            'dates': '',
            'number_of_externs': '',
            'extern_level_preference': '',
            'extern_course_preference': '',
            'requirements': '',
            'name': '',
            'web_address': '',
            'sponsors_job_title': '',
            'externship_location': '',}
    
    #optional_fields = ['housing_assistance', 'transportation_assistance', 'stipend']

    try:
        appCountStr = soup.find(text=re.compile('This externship has'))
        appCount = re.search(r'\b\d+\b', appCountStr).group()
        data['application_count'] = appCount
        tables = soup.findAll('table')
        for table in tables:
            for row in table.findAll('tr'):
                key, val = row.find('th').text, row.find('td').text
                formatKey = format(key)
                data[formatKey] = val
        externship = Externship(**data)
        externship.save()
        #print 'finished', num
    except Exception as e:
        print type(e), e
        print 'failed', num
    


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for idx in range(start, end + 1):
            parse(idx)
