from django.conf.urls import url
from sentiment import views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^analysis$', views.analysis, name='analysis')
]
