from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
	url('^$', TemplateView.as_view(template_name='index.html')),
	url('about.html', TemplateView.as_view(template_name='about.html')),
	url('signatures.html', TemplateView.as_view(template_name='signatures.html')),
	url('petitions.html', TemplateView.as_view(template_name='petitions.html')),
	url('map.html', TemplateView.as_view(template_name='map.html')),
]

