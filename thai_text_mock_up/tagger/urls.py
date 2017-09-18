from django.conf.urls import url
from tagger import views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^analysis$', views.analysis, name='analysis')
]
