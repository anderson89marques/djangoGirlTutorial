from django.conf.urls import url

from mysite.blog.views import post_list, post_show, post_save, post_edit


urlpatterns = [
    url(r'^$', post_list, name='post_list'),
    url(r'show/(?P<pk>(\d+))/$', post_show, name='post_show'),
    url(r'new/$', post_save, name='post_create'),
    url(r'edit/(?P<pk>(\d+))/$', post_edit, name='post_edit'),
]
