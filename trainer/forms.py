from django import forms
from allauth.account.forms import SignupForm
from trainer.models import TrainerIntroduction


class TrainerRegisterForm(SignupForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter full name'}))

	def custom_signup(self, request, user):
		pass