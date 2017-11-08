from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.MemberListView.as_view(), name='view'),
    url(r'^add/$', views.MemberAddView.as_view(), name='add'),
    url(r'^detail/(?P<pk>\d+)$', views.MemberDetailView.as_view(), name='detail'),
    url(r'^edit/(?P<pk>\d+)$', views.MemberEditView.as_view(), name='edit'),
    url(r'^delete/(?P<pk>\d+)$', views.MemberDeleteView.as_view(), name='delete'),
]
