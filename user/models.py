from django.db import models
import re

from django.contrib.auth.models import AbstractUser

# Create your models here.


USER_TYPE_CHOICES = (
	('Trainer', 'Trainer'),
	('RTO', 'RTO')
)


class User(AbstractUser):
	mid_name = models.CharField(max_length=100, blank=True)
	user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES, default='Trainer')


	def name(self):
		full_name = "{} {} {}".format(self.first_name, self.mid_name, self.last_name)
		return re.sub(' +', ' ', full_name)
