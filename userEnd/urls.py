from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'itemDetails/(?P<itemID>\d+)',views.itemDetail, name='detail'),
    url(r'graph/(?P<itemID>\d+)', views.lineGraph, name="graph")
]