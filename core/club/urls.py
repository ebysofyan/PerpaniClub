from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ClubDetailView.as_view(), name='view'),
    url(r'^edit/$', views.ClubEditView.as_view(), name='edit'),
]
