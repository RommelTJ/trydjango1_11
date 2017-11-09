from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from restaurants.views import (
    restaurant_listview,
    RestaurantListView,
    RestaurantDetailView,
    restaurant_createview
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^restaurants/$', RestaurantListView.as_view()),
    url(r'^restaurants/create/$', restaurant_createview),
    url(r'^restaurants/(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view()),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html')),
]
