from django.conf.urls import include, url
from django.views import defaults as default_views

app_name = 'api_v1'

urlpatterns = [
	url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
	url(r'^trainer/', include('trainer.api.v1.urls', namespace='trainer'))
]