from django.db import models
from groups.models import Group
from django.contrib.auth.models import User

class Question(models.Model):
	question_text = models.CharField(max_length=500)
	body = models.CharField(max_length=5000)
	pub_date = models.DateTimeField('date published')
	user = models.ForeignKey(User)
	# group = models.ForeignKey(Group, default=None)
	

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

	
	def __str__(self):
		return self.question_text + str(self.pub_date)

class Answer(models.Model):
	question = models.ForeignKey(Question)
	answer_text = models.CharField(max_length=5000)
	user = models.ForeignKey(User)
	upvotes = models.IntegerField(default=0)

	def upvote(self):
		self.upvotes = self.upvotes + 1
		self.save()

	def downvote(self):
		self.upvotes = self.upvotes - 1
		self.save()

	def __str__(self):
		return self.answer_text
