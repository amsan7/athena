from django.db import models
from groups.models import Group
from django.contrib.auth.models import User

class Question(models.Model):
	question_text = models.CharField(max_length=500)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	user = models.ForeignKey(User)
	group = models.ForeignKey(Group, null=True, blank=True)
	

	MATH = 'Math'
	PHYSICS = 'Physics'
	CHEMISTRY = 'Chemistry'
	BIOLOGY = 'Biology'
	SUBJECT_CHOICES = (
		(MATH, MATH),
		(PHYSICS, PHYSICS),
		(CHEMISTRY, CHEMISTRY),
		(BIOLOGY, BIOLOGY),
	)
	
	subject = models.CharField(max_length=15,
				   choices = SUBJECT_CHOICES,
				   default=MATH)

	def answers_by_vote(self):
		return self.answer_set.order_by('-upvotes')

	def teacher_answers(self):
		users = User.objects.exclude(is_staff = "True")
		teachers = []
		for user in users:
			if user.userprofile.isTeacher:
				teachers.append(user)
		#print teachers
		
		t_answers = self.answer_set.filter(user__in = teachers)
		return t_answers.order_by('-upvotes')

	def student_answers(self):
		users = User.objects.exclude(is_staff = "True")
		students = []
		for user in users:
			if not user.userprofile.isTeacher:
				students.append(user)
		#print teachers
		
		s_answers = self.answer_set.filter(user__in = students)
		return s_answers.order_by('-upvotes')
	
	def __str__(self):
		return self.question_text + str(self.pub_date)

class Answer(models.Model):
	question = models.ForeignKey(Question)
	answer_text = models.TextField()
	user = models.ForeignKey(User)
	upvotes = models.IntegerField(default=0)

	def upvote(self, voter_id):
		self.upvotes = self.upvotes + 1
		self.save()

	def downvote(self, voter_id):
		self.upvotes = self.upvotes - 1
		self.save()

	def __str__(self):
		return self.answer_text
