from django.shortcuts import render, get_object_or_404
from forum.models import Question, Answer
from groups.models import Group
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    my_groups = Group.objects.all()
    context = {
    	'latest_question_list': latest_question_list, 
	'my_groups' : my_groups
	}
    return render(request, 'forum/index.html', context)

def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question no exist :(")
	return render(request, 'forum/detail.html', {'question':question})

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(respone % question_id)

@login_required
def answer(request, question_id):
        q = get_object_or_404(Question, pk=question_id)
        try:
                original_question=Question.objects.get(pk=question_id)
                answer=Answer(
			question=original_question, 
			answer_text=request.POST['answer'],
			user=request.user
			)
               # if request.user.is_authenticated():
               #     user.answers.add(answer)
        except (KeyError, Answer.DoesNotExist):
                #redisplay question form
                return render(request, 'forum/detail', {
                        'question': q,
                        'error_message': "Did not submit an answer!",
                })
        else:
                answer.save()
                #note: always return redirect after dealing with POST data
                return HttpResponseRedirect(reverse('forum:index'))

@login_required
def add_question(request):
        try:
                q = Question(
			question_text=request.POST['question'], 
			pub_date=timezone.now(),
			user=request.user
			)
               # if request.user.is_authenticated():
               #     user.questions.add(q)
        except(KeyError, Question.DoesNotExist):
                return render(request, 'forum/index', {
                        'error_message': "Question must not be empty!",
                })
        else:
                q.save()
                return HttpResponseRedirect(reverse('forum:index'))