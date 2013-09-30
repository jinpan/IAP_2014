from django.http import HttpResponse
from django.shortcuts import render
from django_tables2 import RequestConfig

from IAP_2014.models import Externship
from IAP_2014.tables import ExternshipTable

def home(request):
    table = ExternshipTable(Externship.objects.all())
    RequestConfig(request).configure(table)
    table.paginate(page=request.GET.get('page', 1), per_page=1000)
    context = {
        # 'externships': Externship.objects.all(),
        'externships': table,
    }

    return render(request, 'home.html', context)

def externship(request, id):
    return HttpResponse(str(id))
