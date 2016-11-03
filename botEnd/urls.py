from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r"retrieve",views.valueRetrieve, name="retrieve"),
        url(r'commands/$',views.commandsIndex, name="commands"),
    url(r'commands/(?P<PID>\d+)',views.commandsDetail, name="commandsDetail"),
    url(r'submit/(?P<PID>\d+)/(?P<bs>\w+)/(?P<itemID>\d+)/(?P<amt>\d+)/(?P<price>\d+)/(?P<currentLiquid>\d+)',views.submitTransaction, name="submit")

]