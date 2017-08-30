from django.conf.urls import url, include
from django.contrib import admin
from trainer.views import TrainerRegisterView

urlpatterns = [
    url(r'^register/$', TrainerRegisterView.as_view(), name='register'),
]
