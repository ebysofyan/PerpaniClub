"""perpaniclub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from core.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.LoginView.as_view(), name='login'),
    url(r'^do_logout$', views.LogoutView.as_view(), name='logout'),
    url(r'^error/$', views.ErrorView.as_view(), name='err'),
    url(r'^club/', include('core.club.urls', namespace='club')),
    url(r'^member/', include('core.member.urls', namespace='member')),
    url(r'^documents/', include('core.documents.urls', namespace='docs')),
    url(r'^setting/', include('core.socialsetting.urls', namespace='setting')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
