from rest_framework import serializers
from django.contrib.auth.models import User
from .models import DailyEvent, DailyLesson, TongueTwister

############
## Events ##
############

class TongueTwisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TongueTwister
        fields = '__all__'
        # fields = ('id', 'username')


class DailyLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLesson
        fields = '__all__'
        # fields = ('id', 'shortname')


class DailyEventSerializer(serializers.ModelSerializer):
    daily_lesson = DailyLessonSerializer(many=True)
    
    class Meta:
        model = DailyEvent
#        depth = 1
        fields = ('target_language', 'level', 'dayNumber', 'daily_lesson')
