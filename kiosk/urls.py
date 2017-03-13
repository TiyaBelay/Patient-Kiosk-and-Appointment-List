from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
]
