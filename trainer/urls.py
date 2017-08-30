from django.conf.urls import url, include
from django.contrib import admin
from trainer.views import TrainerRegisterView, TrainerDashboardView

urlpatterns = [
    url(r'^register/$', TrainerRegisterView.as_view(), name='register'),

    url(r'^dashboard/$', TrainerDashboardView.as_view(), name='dashboard'),
]
