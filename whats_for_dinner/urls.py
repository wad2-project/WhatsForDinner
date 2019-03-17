from django.conf.urls import url
from whats_for_dinner import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^result/$', views.result, name='result'),
]
