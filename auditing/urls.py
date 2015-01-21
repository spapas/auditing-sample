from django.conf.urls import patterns, include, url
from django.contrib import admin

from sample.views import BookCreateView, SHBookCreateView, RBookCreateView, BookUpdateView, SHBookUpdateView, RBookUpdateView, BookListView, SHBookListView, RBookListView, HomeTemplateView

urlpatterns = patterns('',

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'account/login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'account/logout.html'}),

    url(r'^$', HomeTemplateView.as_view(), name='book_list'),

    url(r'^create/$', BookCreateView.as_view(), name='create_book'),
    url(r'^create_sh/$', SHBookCreateView.as_view(), name='create_shbook'),
    url(r'^create_r/$', RBookCreateView.as_view(), name='create_rbook'),
    url(r'^update/(?P<pk>\d+)/$', BookUpdateView.as_view(), name='update_book'),
    url(r'^update_sh/(?P<pk>\d+)/$', SHBookUpdateView.as_view(), name='update_shbook'),
    url(r'^update_r/(?P<pk>\d+)/$', RBookUpdateView.as_view(), name='update_rbook'),
    url(r'^books/$', BookListView.as_view(), name='book_list'),
    url(r'^shbooks/$', SHBookListView.as_view(), name='shbook_list'),
    url(r'^rbooks/$', RBookListView.as_view(), name='rbook_list'),

    url(r'^admin/', include(admin.site.urls)),
)
