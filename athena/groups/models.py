from django.db import models

class Group(models.Model):
	# GROUP ID?
	group_name = models.CharField(max_length=5000)
	create_date = models.DateTimeField('date created')
	# user = models.ForeignKey(User) #group creator (has power to delete group/etc)
	topic = models.CharField(max_length=500)
	def __str__(self):
		return self.group_name


class GroupUserJoin(models.Model):
	# user = models.ForeignKey(User)
	group = models.ForeignKey(Group)