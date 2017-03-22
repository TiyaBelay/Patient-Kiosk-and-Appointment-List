from django.conf.urls import include, url
from django.contrib import admin

import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^authorize/$', views.authorize, name='authorize'),
    url(r'^login/$', views.drchrono_login, name='drchrono_login'),
    url(r'^logout/$', views.drchrono_logout, name='drchrono_logout'),
    url(r'^home/$', views.home, name='home'),
    url(r'^check_in/$', views.check_in, name="check_in"),
    url(r'^demographic/$', views.patient_demographic, name='demographic'),
    url(r'^appointments/$', views.appointments, name='appointments'),
    url(r'^checked_in/$', views.checked_in, name="checked_in"),
    url(r'', include('social.apps.django_app.urls', namespace='social')),

]
