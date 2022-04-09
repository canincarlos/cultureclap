import os
import time
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from versatileimagefield.fields import VersatileImageField

from django.core.files.storage import FileSystemStorage

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


def music_full_audio_file(instance, filename):
    file_path = 'tongue-twister/{lang}/{shortname}/{full_audio}'.format(
         lang=instance.target_language, 
         shortname=instance.shortname.replace(' ', ''), 
         full_audio=instance.audio) 
    return file_path


class DailyEvent(models.Model):
	TARGET_LANG_CHOICE = (
            (0, 'English'),
            (1, 'Spanish'),
            )
	TARGET_LANG_LEVEL = (
            (0, 'Basics I'),
            (1, 'Basics II'),
            (2, 'Intermediate'),
            )
	target_language = models.PositiveSmallIntegerField(choices=TARGET_LANG_CHOICE, default=0)
	level = models.PositiveSmallIntegerField(choices=TARGET_LANG_LEVEL, default=0)
	dayNumber = models.PositiveSmallIntegerField(blank=True, null=True)
	published = models.BooleanField(default=False)


	class Meta:
		verbose_name_plural = "Daily Events"
		ordering = ['level', 'dayNumber']

	def __unicode__(self):
		return "/%s/%s/%s/" % self.target_language, self.level, self.dayNumber

	def __str__(self):
		return u'/%s/%s/%s/' % self.target_language, self.level, self.dayNumber


class DailyLesson(models.Model):
    shortname = models.CharField(max_length=64, blank=True, null=True)
    lessonEnglish = models.TextField(blank=True, null=True)
    lyrics_trans = models.TextField(blank=True, null=True)
    dayNumber = models.ForeignKey('DailyEvent', related_name='daily_event', blank=True, null=True, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = "Daily Lessons"
        ordering = ['published', 'shortname']

    def __unicode__(self):
        return "/dailyLessons/%s-%s/" % self.dayNumber, self.shortname

    def __str__(self):
        return u'%s-%s' % self.dayNumber, self.shortname


class TongueTwister(models.Model):
	TARGET_LANG_CHOICE = (
            (0, 'English'),
            (1, 'Spanish'),
            )
	target_language=models.PositiveSmallIntegerField(choices=TARGET_LANG_CHOICE, default=0)
	audio = models.FileField(upload_to=music_full_audio_file, blank=True, null=True)
	shortname = models.CharField(max_length=64, blank=True, null=True)
	tl_text = models.TextField(blank=True, null=True)
	phonetic_text = models.TextField(blank=True, null=True)
	text_trans = models.TextField(blank=True, null=True)
	published = models.BooleanField(default=False)


	class Meta:
		verbose_name_plural = "Tongue Twisters"
		ordering = ['target_language', 'published', 'shortname']

	def __unicode__(self):
		return "/tongue-twisters/%s/%s/" % self.target_language, self.shortname

	def __str__(self):
		return u'%s-%s' % self.target_language, self.shortname


# class Video(models.Model):
#     TARGET_LANG_CHOICE = (
#             (0, 'English'),
#             (1, 'Spanish'),
#             )

#     title = models.CharField(max_length=255)
#     artist = models.CharField(max_length=255)
#     music_genre = models.ForeignKey(MusicGenre, on_delete=models.PROTECT, blank=True, null=True)
#     pub_date = models.DateTimeField(auto_now_add=True)
#     target_language=models.PositiveSmallIntegerField(choices=TARGET_LANG_CHOICE, default=0)
#     full_audio = models.FileField(upload_to=music_full_audio_file, blank=True, null=True)
#     link = models.CharField(max_length=255, unique=True, blank=True, null=True)
#     slug = models.SlugField(unique=True, max_length=255)
#     published = models.BooleanField(default=False)
#     submitted_by = models.ForeignKey(User, on_delete=models.PROTECT)
# #    category = models.ForeignKey(Category, blank=True, null=True, on_delete="PROTECT")
# #    tags = models.ManyToManyField(Tag, blank=True)

#     class Meta:
#         ordering = ['-pub_date']

#     def __unicode__(self):
#         return u'%s' % self.title

#     def __str__(self):
#         return u'%s' % self.title

#     def get_absolute_url(self):
#         return "/%s/" % (self.slug)