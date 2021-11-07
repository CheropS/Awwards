from django.conf.urls import url 
from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$', views.home, name='home'),
    url('^new/$',views.create_post,name = 'new-projects'),
    url('^project/$',views.viewProject,name = 'view-project'),
    url('^search/', views.search_results, name='search_results'),
    url('^profile/', views.profile, name='profile'),
    # url('^ratings/(?P<pk>\d{10,18})/$/', views.rateProject, name='ratings'),
   path('ratings/<int:pk>/', views.rateProject, name='ratings')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)