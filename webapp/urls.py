from django.conf.urls import url
from . import views
from webapp.views import Purchase


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^purchase$', Purchase.as_view()),
    ]
