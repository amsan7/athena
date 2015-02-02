from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
	question_text = models.CharField(max_length=5000)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text + str(self.pub_date)

class Answer(models.Model):
	question = models.ForeignKey(Question)
	answer_text = models.CharField(max_length=5000)
	def __str__(self):
		return self.answer_text

class UserProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to='profile_images', blank=True)
    #TODO: add a constant val for max_length
    school = models.CharField(max_length=500)

    groups = models.ManyToManyField(Groups)
    #TODO:
    # add fields for questions
    # add fields for answers
    # add fields for database
    # Override the __unicode__() method to return out something meaningful
    def __unicode__(self):
        return self.user.username

