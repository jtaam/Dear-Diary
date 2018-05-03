from django.shortcuts import render
from .models import Entry


def index(request):
    entries = Entry.objects.order_by('-date_posted')
    context = {'entries': entries}
    return render(request, 'entries/index.html', context)


def add(request):
    return render(request, 'entries/add.html')


