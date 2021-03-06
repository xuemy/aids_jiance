from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

urlpatterns = [
                  url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
                  url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),
                  url(r'^help/$', TemplateView.as_view(template_name='pages/help.html'), name='help'),

                  url(r'^zice/$', TemplateView.as_view(template_name='pages/zice.html'), name='zice'),
                  url(r'^shiyong/$', TemplateView.as_view(template_name='pages/shizhishiyong.html'), name='shiyong'),

                  # Django Admin, use {% url 'admin:index' %}
                  url(settings.ADMIN_URL, admin.site.urls),

                  # Your stuff: custom urls includes go here
                  url(r'^a/', include('aids_jiance.article.urls', namespace='article')),
                  url(r'^shizhi/', include('aids_jiance.shizhi.urls')),

                  url(r'^ckeditor/', include('ckeditor_uploader.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [url(r'^__debug__/', include(debug_toolbar.urls)), ] + urlpatterns
