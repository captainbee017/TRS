from django.shortcuts import render
from allauth.account.views import SignupView
from trainer.forms import TrainerRegisterForm
from django.views.generic import TemplateView

# Create your views here.


class TrainerRegisterView(SignupView):
	template_name = 'trainer_signup.html'

	def get_form_class(self):
		return TrainerRegisterForm


class TrainerDashboardView(TemplateView):
	template_name = 'trainer_dashboard.html'