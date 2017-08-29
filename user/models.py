from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
	mid_name = models.CharField(max_length=100)


	def name(self):
		if self.mid_name:
			return "{} {} {}".format(self.first_name, self.mid_name, self.last_name)
		return "{} {}".format(self.first_name, self.last_name)