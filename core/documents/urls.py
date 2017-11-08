from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.DocumentsView.as_view(), name='view'),
    url(r'^delete/(?P<pk>\d+)$', views.DocumentDelete.as_view(), name='delete'),
]
