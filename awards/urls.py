from django.conf.urls import url 
from . import views 

urlpatterns=[
    url('^$', views.home, name='home'),
    url('^new/$',views.create_post,name = 'new-projects'),
]