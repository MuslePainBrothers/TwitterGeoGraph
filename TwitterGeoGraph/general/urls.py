from django.conf.urls import url
from . import views

app_name = 'general'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^top$', views.TopView.as_view(), name="top"),
    url(r'^clawler$', views.clawlerTwitter, name="clawler"),
    url(r'^map$', views.MapView.as_view(), name="map"),
]