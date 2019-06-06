from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^', views.devs, name='devs'),
    url(r'^signup',views.signup, name='signup'),
    url(r'user/(?P<username>\w+)', views.profile,name='profile'),
    url(r'^upload/$', views.upload_post, name='upload_post'),
    url(r'^accounts/edit/',views.edit_profile, name='edit_profile'),
    url(r'^search/', views.search, name='search')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)