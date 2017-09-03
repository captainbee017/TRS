import re
from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


USER_TYPE_CHOICES = (
	('Trainer', 'Trainer'),
	('RTO', 'RTO')
)


class User(AbstractUser):
	mid_name = models.CharField(max_length=100, blank=True)
	user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES, default='Trainer')

	@property
	def name(self):
		full_name = "{} {} {}".format(self.first_name, self.mid_name, self.last_name)
		full_name = re.sub(' +', ' ', full_name)
		return full_name

	def __str__(self):
		return self.name

	def is_trainer():
		return self.user_type == 'Trainer'

	def is_rto():
		return self.user_type == 'RTO'
