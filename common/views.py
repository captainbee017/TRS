from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View

# Create your views here.

class SelectLoginView(View):
	def get(self, request, *args, **kwargs):
		if request.user.is_trainer():
			return 	redirect('trainer:login')
		return redirect('landing_page')


class LandingPageView(TemplateView):
	template_name = 'landing_page.html'