from django.conf.urls import include, url
from trainer.api.v1.views import TrainerIntroductionList, TrainerIntroductionDetail

urlpatterns = [
	url(r'^introduction/list/$', 
		TrainerIntroductionList.as_view(), name='introduction_list'),
	url(r'^introduction/detail/(?P<pk>\d+)/$', 
		TrainerIntroductionDetail.as_view(), name='introduction_detail'),
]