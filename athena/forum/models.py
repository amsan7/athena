from django.db import models
from groups.models import Group
from django.contrib.auth.models import User

class Question(models.Model):
	question_text = models.CharField(max_length=5000)
	pub_date = models.DateTimeField('date published')
	user = models.ForeignKey(User)
	# group = models.ForeignKey(Group, default=None)
	def __str__(self):
		return self.question_text + str(self.pub_date)

class Answer(models.Model):
	question = models.ForeignKey(Question)
	answer_text = models.CharField(max_length=5000)
	user = models.ForeignKey(User)
	upvotes = models.IntegerField(default=0)
	def __str__(self):
		return self.answer_text