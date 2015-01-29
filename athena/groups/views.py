from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'groups/index.html')

def detail(request, group_id):
	return render(request, 'groups/detail.html')