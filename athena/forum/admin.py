from django.contrib import admin
from forum.models import Question, Answer, UserProfile

admin.site.register(Question)
admin.site.register(UserProfile)
