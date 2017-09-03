from django.db import models
from user.models import User
from common.models import Location

# Create your models here.

class TrainerIntroduction(models.Model):
    """
    Trainer Basic Information
    """
    user = models.OneToOneField(User)
    headline = models.CharField(max_length=100)
    current_position = models.CharField(max_length=100)
    address = models.ForeignKey(Location)
    summary = models.TextField()

    def __str__(self):
        return self.user.name


class TrainerWorkExperience(models.Model):
  trainer = models.ForeignKey(TrainerIntroduction, related_name='work_experiences')
  org_name = models.CharField(max_length=100)
  designation = models.CharField(max_length=100)

  def __str__(self):
    return self.trainer


class ExpVocationalExperience(models.Model):
    role = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    # attachments = models.FieldField(upload_to='uploads/trainer/vocational_exp')

    def __str__(self):
        return self.role


class Qualification(models.Model):
    code = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    issuing_rto = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=False)
    certificate_number = models.CharField(max_length=200)

    class Meta:
        abstract = True


class ExpAssessmentQualification(Qualification):
    work_experience = models.ForeignKey(TrainerWorkExperience)

    def __str__(self):
        return self.code

class ExpVocationQualification(models.Model):
    work_experience = models.ForeignKey(TrainerWorkExperience)
    course_name = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.work_experience