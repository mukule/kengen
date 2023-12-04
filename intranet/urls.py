
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Intranet Administration Panel'
admin.site.index_title = 'Intranet Application Administrations'


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    # path("", include('main.urls')),
    path("", include('users.urls')),
    path("news/", include('news.urls', namespace='news')),
    path('articles/', include('articles.urls')),
    path('tinymce/', include('tinymce.urls')),
    path("core/", include('core.urls', namespace='core')),
    path("events/", include('events.urls', namespace='events')),
    path("tasks/", include('tasks.urls', namespace='tasks')),
    path("documents/", include('documents.urls', namespace='documents')),
    path("applications", include('applications.urls', namespace='applications')),
    path("facilities", include('facilities.urls', namespace='facilities')),
    path("messaging/", include('messaging.urls', namespace='messaging')),
    path("polls/", include('polls.urls', namespace='polls')),
    path("adminstration/", include('adminstration.urls', namespace='adminstration')),
  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
