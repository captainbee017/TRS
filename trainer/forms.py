from django import forms
from allauth.account.forms import SignupForm
from trainer.models import TrainerIntroduction


class TrainerRegisterForm(SignupForm):
	name = forms.CharField(
		required=True,
		widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
	contact_number = forms.CharField(
		required=True,
		widget=forms.TextInput(attrs={'placeholder': 'Contact Number'}))

	def custom_signup(self, request, user):
		super().custom_signup(request, user)
		user.user_type = 'Trainer'
		first_name, mid_name, last_name = self.get_names()
		user.first_name = first_name
		if mid_name:
			user.mid_name = mid_name
		if last_name:
			user.last_name = last_name
		user.save()

	def get_names(self):
		names = self.cleaned_data['name'].split(' ')
		first_name, mid_name, last_name = None, None, None
		if len(names) == 1:
			first_name = names[0]
		elif len(names) > 2:
			first_name = names[0]
			mid_name = ' '.join(names[1:-1])
			last_name = names[-1]
		else:
			first_name= names[0]
			last_name = names[-1]
		return first_name, mid_name, last_name
