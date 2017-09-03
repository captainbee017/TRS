from django.conf.urls import url, include
from django.contrib import admin
from trainer.views import TrainerLoginView, TrainerRegisterView, TrainerDashboardView

urlpatterns = [
    url(r'^register/$', TrainerRegisterView.as_view(), name='register'),
    url(r'^login/$', TrainerLoginView.as_view(), name='login'),

    url(r'^dashboard/$', TrainerDashboardView.as_view(), name='dashboard'),
]
