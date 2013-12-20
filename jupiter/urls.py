from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.conf import settings

from jupiter.views import ReadingCreate, PhysicalActivityCreate
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

    url(r'^activity/create$', PhysicalActivityCreate.as_view(), name='physical_activity_create')
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
