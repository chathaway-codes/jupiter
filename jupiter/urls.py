from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.conf import settings

from jupiter.views import ReadingCreate, PhysicalActivityCreate
from jupiter.views import ActivityCreate
from jupiter.views import UserDetail, UserVisualize, UserEdit

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # TemplateView + Login
    url(r'^$', TemplateView.as_view(template_name="home.html"), {}, 'home'),
    #url(r'^$', login_required(TemplateView.as_view(template_name="home.html")), {}, 'home'),


    # Views for stuff and things
    url(r'^reading/create$', ReadingCreate.as_view(), name='reading_create'),

    url(r'^user/edit$', UserEdit.as_view(), name='user_edit'),

    url(r'^dashboard$', UserDetail.as_view(), name='user_detail'),

    url(r'^user/(?P<pk>\d+)/visualize$', UserVisualize.as_view(), name='user_vidualize'),

    url(r'^physical_activity/create$', PhysicalActivityCreate.as_view(), name='physical_activity_create'),

    url(r'^activity/create$', ActivityCreate.as_view(), name='activity_create'),

    url(r'^activity/location$', TemplateView.as_view(template_name="jupiter/location.html"), name='activity_locator'),



    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'home.html'}),
    url(r'^accounts/register/$', RegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/chpasswd/done/?', 'django.contrib.auth.views.password_change_done', {'template_name':'password_change_done.html'}),
    url(r'^accounts/change/password/?', 'django.contrib.auth.views.password_change', {'template_name':'change_password.html', 'post_change_redirect': '/accounts/chpasswd/done/' }, name="change_password"),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
