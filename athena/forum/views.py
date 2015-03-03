from django.shortcuts import render, get_object_or_404
from forum.models import Question, Answer
from groups.models import Group
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from json import dumps, loads


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    my_groups = Group.objects.all()
    context = {
    	'latest_question_list': latest_question_list, 
	'my_groups' : my_groups,
	'subject_choices' : [subject[0] for subject in Question.SUBJECT_CHOICES]
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

@csrf_exempt
def upvote(request, question_id = 0):
    if request.method == 'POST':
        answer_id = request.POST.get('a_id')
        answer=Answer.objects.get(pk=answer_id)
        response_data = {}
        answer.upvote()
        response_data['answerpk'] = answer.pk
        response_data['upvotes'] = answer.upvotes

        return HttpResponse(
            dumps(response_data),
            content_type = "application/json"
        )

@csrf_exempt
def downvote(request, question_id = 0):
    if request.method == 'POST':
        answer_id = request.POST.get('a_id')
        answer=Answer.objects.get(pk=answer_id)
        response_data = {}
        answer.downvote()
        response_data['answerpk'] = answer.pk
        response_data['upvotes'] = answer.upvotes

        return HttpResponse(
            dumps(response_data),
            content_type = "application/json"
        )

@login_required
@csrf_exempt
def answer(request, question_id = 0):
    if request.method == 'POST':
        answer_text = request.POST.get('answer_text')
        question_id = request.POST.get('q_id')
        original_question=Question.objects.get(pk=question_id)
        response_data = {}
        answer=Answer(
           question=original_question, 
           answer_text=answer_text,
           user=request.user
        )
        answer.save()
        response_data['answer_id'] = answer.pk
        response_data['votes'] = answer.upvotes
        response_data['answer_text'] = answer.answer_text
        response_data['answer_username'] = answer.user.username
        response_data['answer_user_id'] = answer.user.id
        response_data['is_teacher'] = "Student"
        if answer.user.userprofile.isTeacher:
            response_data['is_teacher'] = "Teacher"

        return HttpResponse(
            dumps(response_data),
            content_type = "application/json"
        )

#        q = get_object_or_404(Question, pk=question_id)
#        try:
#                original_question=Question.objects.get(pk=question_id)
#                answer=Answer(
#			question=original_question, 
#			answer_text=request.POST['answer'],
#			user=request.user
#			)
#               # if request.user.is_authenticated():
#               #     user.answers.add(answer)
#        except (KeyError, Answer.DoesNotExist):
#                #redisplay question form
#                return render(request, 'forum/detail', {
#                        'question': q,
#                        'error_message': "Did not submit an answer!",
#                })
#        else:
#                answer.save()
#                #note: always return redirect after dealing with POST data
#                return HttpResponseRedirect(reverse('forum:index'))

@login_required(redirect_field_name='banana')
def add_question(request):
        try:
                q = Question(
			question_text=request.POST['question'], 
			body = request.POST['body'],
			pub_date=timezone.now(),
			user=request.user,
			subject=request.POST['subject']
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
