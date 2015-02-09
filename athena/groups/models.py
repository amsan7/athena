from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
	group_name = models.CharField(max_length=5000)
	create_date = models.DateTimeField('date created')
	creator_username = models.CharField(max_length=5000)#group creator (has power to delete group/etc)
	group_members = models.ManyToManyField(User)
	# questions = models.OneToManyField()
	topic = models.CharField(max_length=500)
	def __str__(self):
		return self.group_name

# class GroupUserJoin(models.Model):
# 	user = models.ForeignKey(User, null=True)
# 	group = models.ForeignKey(Group)