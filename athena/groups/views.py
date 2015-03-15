from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from groups.models import Group
from forum.models import Question, Answer
from users.models import UserProfile
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def index(request):
    my_groups = Group.objects.all()
    context = {'my_groups' : my_groups}
    return render(request, 'groups/index.html', context)

@login_required
# give only people in the group permission to see it
def detail(request, group_id):
    try:
        group = Group.objects.get(pk=group_id)
    except Group.DoesNotExist:
        raise Http404("Group no exist :(")
    context = {
        'group' : group,
        'latest_question_list' : Question.objects.filter(group=group).order_by('-pub_date'),
        'subject_choices' : [subject[0] for subject in Question.SUBJECT_CHOICES]
    }
    return render(request, 'groups/detail.html', context)

def new(request):
    all_users = User.objects.all()
    context = {'all_users' : all_users,
    'group_choices' : [type[0] for type in Group.GROUP_CHOICES]
    }
    return render(request, 'groups/new.html', context)

# def edit(request, group_id):
#     try:
#         group = Group.objects.get(pk=group_id)
#     except(KeyError, Group.DoesNotExist):
#         return render(request, '/forum/index', {
#             'error_message': "!",
#             })
#     else:
        

# def delete(request, group_id):
#     try:
#         group = Group.objects.get(pk=group_id)
#     except(KeyError, Group.DoesNotExist):
#         return render(request, '/forum/index', {
#             'error_message': "!",
#             })
#     else:
        
@login_required
def add_group(request):
    print("checkbox input field")
    print(request.POST.getlist('members'))
    try:
        g = Group(
            group_name=request.POST['group_name'], 
            topic=request.POST['topic'], 
            create_date=timezone.now(),
            creator_username=request.user.username
            )
        g.save()
        groupMembers = request.POST.getlist('members')
        for u in groupMembers:
            print u
            print UserProfile.objects.get(pk=u)
            g.group_members.add(UserProfile.objects.get(pk=u))
        # g.group_members.add(UserProfile.objects.get(pk=request.POST.getlist('members')))

    except(KeyError, Group.DoesNotExist):
        return render(request, '/forum/index', {
            'error_message': "!",
            })
    else:
        g.save()
        return HttpResponseRedirect(reverse('forum:index'))
        return render()













