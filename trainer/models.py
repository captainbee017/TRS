from django.db import models
from users.models import User
from common.models import Location

# Create your models here.

class TrainerIntroduction(models.Model):
	user = models.OneToOneField(User)
	headline = models.CharField(max_length=100)
	current_position = models.CharField(max_length=100)
	address = models.ForeignKey(Location)
	summary = models.TextField()


# class TrainerEducation(models.Model):
# 	trainer = models.ForeignKey(TrainerIntroduction, related_name='educations')


# class TrainerWorkExperience(models.Model):
# 	trainer = models.ForeignKey(TrainerIntroduction, related_name='work_experiences')
# 	org_name = models.CharField(max_length=100)
# 	designation = models.CharField(max_length=100)
