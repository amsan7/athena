from django.db import models
from django.contrib.auth.models import User
# from forum.models import Answer

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

    # upvotedAnswers = models.ManyToManyField(Answer, related_name='upvotedAnswers')

    # downvotedAnswers = models.ManyToManyField(Answer, related_name='downvotedAnswers')
    def upvoted(self, answer):
        all_upvoted = self.upvotedAnswers.all()
        #print all_upvoted
        if answer in all_upvoted:
            return True
        else:
            return False

    def upvote(self, answer):
        self.upvotedAnswers.add(answer)
        self.save()

    def rm_upvote(self, answer):
        self.upvotedAnswers.remove(answer)
        self.save()

    def downvoted(self, answer):
        all_downvoted = self.downvotedAnswers.all()
        #print all_downvoted
        if answer in all_downvoted:
            return True
        else:
            return False

    def downvote(self, answer):
        self.downvotedAnswers.add(answer)
        self.save()

    def rm_downvote(self, answer):
        self.downvotedAnswers.remove(answer)
        self.save()

    #TODO:
    # add fields for database
    # Override the __unicode__() method to return out something meaningful
    def __unicode__(self):
        return self.user.username
