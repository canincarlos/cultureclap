from django.conf.urls import url
from django.views.generic import DetailView
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [ 
     url(r'^api/searchtts$', GetTTwistersAPIView.as_view(), name="get-tts"),    
     url(r'^api/lessons$', LessonAPIView.as_view(), name="lessons"),
     url(r'^api/event$', EventAPIView.as_view(), name="lessons"),
     # url(r'^api/ivid/[-@\w]+/$', VideoAPIView.as_view(), name="video"),
    # url(r'^(?P<pk>[0-9]+)/update/$', officer_update),    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns = format_suffix_patterns(urlpatterns)
