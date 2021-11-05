from django.conf.urls import url 
from . import views 

urlpatterns=[
    url('^$', views.home, name='home'),
    url('^new/$',views.create_post,name = 'new-projects'),
    url('^project/$',views.viewProject,name = 'view-project'),
    url('^search/', views.search_results, name='search_results'),
    url('^profile/', views.profile, name='profile'),
   
]