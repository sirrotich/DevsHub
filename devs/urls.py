from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^devs', views.devs, name='devs'),
    url(r'^signup',views.signup, name='signup'),
    url(r'user/(?P<username>\w+)', views.profile,name='profile'),
    url(r'^upload/$', views.upload_post, name='upload_post'),
    url(r'^accounts/edit/',views.edit_profile, name='edit_profile'),
    url(r'^post/(?P<post_id>\d+)', views.single_post, name='single_post'),
    url(r'^search/', views.search, name='search')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)