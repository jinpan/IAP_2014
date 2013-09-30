"""
This script downloads pages from the externship postings page
"""

from django.core.management.base import BaseCommand
from requests import get



base_url = 'https://alum.mit.edu/externship/2014/applicant/externship/%d'
base_loc = '/home/jin/Projects/IAP_2014/pages/%d.html'

start, end = 4841, 5301
cookie = {'JSESSIONID': '0840eab6647dd15eb1db19d30354'}


def save(response, filename):
    text = response.content
    with open(filename, 'wb') as f:
        f.write(text)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for idx in range(start, end + 1):
            response = get(base_url % idx, cookies=cookie)
            save(response, base_loc % idx)

