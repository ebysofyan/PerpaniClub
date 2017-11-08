from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.SocialSettingView.as_view(), name='view'),
    url(r'^edit/(?P<pk>\d+)$', views.SocialSettingEditView.as_view(), name='edit'),
    url(r'^delete/(?P<pk>\d+)$', views.SocialSettingDeleteView.as_view(), name='delete'),
]
