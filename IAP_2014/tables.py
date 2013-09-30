from django_tables2 import Column
from django_tables2 import tables
from django_tables2.columns import URLColumn

from IAP_2014.models import Externship

class URLColumn2(URLColumn):
    def render(self, value):
        # first arg is the href, second is the display
        base_url = 'https://alum.mit.edu/externship/2014/applicant/externship/%d'
        return self.render_link(base_url % value, value)


class ExternshipTable(tables.Table):
    class Meta:
        model = Externship
        attrs = {'class': 'paleblue'}
        
        exclude = (
            'url',
            'description',
            'dates',
            'requirements',
            'sponsors_job_title',
            )

    id = URLColumn2()

