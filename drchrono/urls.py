from django.conf.urls import include, url
from django.contrib import admin

import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.drchrono_login, name='drchrono_login'),
    url(r'^logout/$', views.drchrono_logout, name='drchrono_logout'),
    url(r'^home/$', views.home, name='home'),
    url(r'^demographic/$', views.patient_chart, name='patient'),
    url(r'', include('social.apps.django_app.urls', namespace='social')),

]
