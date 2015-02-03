from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from groups.models import Group, GroupUserJoin
from forum.models import UserProfile
from django.utils import timezone


def index(request):
    my_groups = Group.objects.all()
    context = {'my_groups' : my_groups}
    return render(request, 'groups/index.html', context)

def detail(request, group_id):
    try:
        group = Group.objects.get(pk=group_id)
    except Group.DoesNotExist:
        raise Http404("Group no exist :(")
    return render(request, 'groups/detail.html', {'group':group})

def new(request):
    return render(request, 'groups/new.html')

def add_group(request):
    try:
        curr_user=UserProfile.objects.all()[0]
        g = Group(group_name=request.POST['group_name'], topic=request.POST['topics'], create_date=timezone.now())
    except(KeyError, Group.DoesNotExist):
        return render(request, '/forum/index', {
            'error_message': "!",
            })
    else:
        g.save()
        return HttpResponseRedirect(reverse('forum:index'))
        return render()