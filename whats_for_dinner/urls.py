from django.conf.urls import url
from whats_for_dinner import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.about, name='about'),
    url(r'^$', views.result, name='result'),
]
