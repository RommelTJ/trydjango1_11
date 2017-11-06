from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from restaurants.views import HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html')),
]
