from django.db import models
# from forum.models import UserProfile

class Group(models.Model):
	group_name = models.CharField(max_length=5000)
	create_date = models.DateTimeField('date created')
	# user = models.ForeignKey(UserProfile) #group creator (has power to delete group/etc)
	topic = models.CharField(max_length=500)
	def __str__(self):
		return self.group_name

class GroupUserJoin(models.Model):
	# user = models.ForeignKey(UserProfile)
	group = models.ForeignKey(Group)