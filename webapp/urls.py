from django.conf.urls import url
from . import views
from webapp.views import Purchase
from . import viewsAddBarcode
from webapp.views import BarcodeView


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^purchase$', Purchase.as_view()),
    url(r'^barcode$', BarcodeView.as_view()),
    ]
