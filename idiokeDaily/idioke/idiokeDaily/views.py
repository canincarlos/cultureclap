from django.shortcuts import render
from pprint import pprint as ppr
# Create your views here.
from datetime import datetime, timedelta
import pytz
import random

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, EmptyPage
from django.views.generic import ListView
from django.db.models import Q

from .models import DailyEvent, DailyLesson, TongueTwister
from .serializers import *
from django.contrib.auth.models import User

from rest_framework.settings import api_settings
from rest_framework import generics
from rest_framework.views import APIView

from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

tz_format = '%Y-%m-%dT$H:%M:%S+%H:%M'
odt = datetime.now()
ndt = odt.strftime(tz_format)

############
## Search ##
############
# @permission_classes([])
# @authentication_classes([])
# class SearchVideosAPIView(generics.ListAPIView):
#     serializer_class = VideoSerializer

#     def get_queryset(self):
#         queryset = Video.objects.all()
#         video_query = self.request.query_params.get('q', None)
#         if video_query is not None:
#             queryset = queryset.filter(Q(published=True) & 
#                 Q(title__icontains=video_query)|
#                 Q(artist__icontains=video_query)               
#             ).distinct()
#         return queryset


@permission_classes([])
@authentication_classes([])
class GetTTwistersAPIView(generics.ListAPIView):
    serializer_class = TongueTwisterSerializer
    def get_queryset(self):
        queryset = TongueTwister.objects.filter(published=True)
        rndm = random.sample(range(len(queryset)), 1)
        tt = queryset[rndm]
        return tt


@permission_classes([])
@authentication_classes([])
class LessonAPIView(generics.ListAPIView):
    serializer_class = DailyLessonSerializer
    queryset = DailyLesson.objects.all()


@permission_classes([])
@authentication_classes([])
class EventAPIView(generics.ListAPIView):
    serializer_class = DailyEventSerializer
    queryset = DailyEvent.objects.all()