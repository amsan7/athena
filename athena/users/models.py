from django.db import models
from forum.models import Question, Answer
from groups.models import Group
from django.contrib.auth.models import User

class UserProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    picture = models.CharField(max_length=5000, default='Paste image URL here')
    #TODO: add a constant val for max_length
    school = models.CharField(max_length=500, default='school')

    isTeacher = models.BooleanField(default=False)

    firstName = models.CharField(max_length=500, default='first name')

    lastName = models.CharField(max_length=500, default='last name')

    # field for questions
    questions = models.ManyToManyField(Question)

    # field for answers
    answers = models.ManyToManyField(Answer)

    # field for groups
    groups = models.ManyToManyField(Group)


    #TODO:
    # add fields for database
    # Override the __unicode__() method to return out something meaningful
    def __unicode__(self):
        return self.user.username
