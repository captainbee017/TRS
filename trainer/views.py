from django.shortcuts import render
from allauth.account.views import SignupView
from trainer.forms import TrainerRegisterForm

# Create your views here.


class TrainerRegisterView(SignupView):
	template_name = 'trainer_signup.html'

	def get_form_class(self):
		return TrainerRegisterForm
	