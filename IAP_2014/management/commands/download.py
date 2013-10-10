"""
This script downloads pages from the externship postings page
"""

from django.core.management.base import BaseCommand
from requests import get
import os

base_url = 'https://alum.mit.edu/externship/2014/applicant/externship/%d'
base_loc = 'listings/%d.html'

start, end = 4841, 5358
cookie = {'JSESSIONID': '0fd1fded35bf784b242971bf9025'}

def save(response, filename):
    text = response.content
    with open(filename, 'wb') as f:
        f.write(text)

def delete_empty_listings(dir):
    for fname in os.listdir(dir):
        fname = dir+'/'+fname
        remove = False
        if fname[-5:] == '.html':
            try:
                f = open(fname)
            except:
                continue
            if "cannot be found" in f.read():
                remove = True
            f.close()
            if remove:
                os.remove(fname)

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for idx in range(start, end + 1):
            response = get(base_url % idx, cookies=cookie)
            save(response, base_loc % idx)
        delete_empty_listings(base_loc[:-7])


