from django.db import models
from django.contrib.auth.models import User
import time
import os

CITY_CHOICES = (
    ('Mataram', 'Mataram'),
    ('Lombok Barat', 'Lombok Barat'),
    ('Lombok Tengah', 'Lombok Tengah'),
    ('Lombok Timur', 'Lombok Timur'),
    ('Lombok Utara', 'Lombok Utara'),
    ('Sumbawa', 'Sumbawa'),
    ('Sumbawa Barat', 'Sumbawa Barat'),
    ('Bima', 'Bima'),
    ('Dompu', 'Dompu'),
)


def file_profile(instance, filename):
    ext = filename.split('.')[-1]
    milis = int(round(time.time()))
    filename = "%s.%s" % (str(milis), ext)
    return os.path.join('user/profile', filename)


def file_club(instance, filename):
    name, ext = filename.split('.')[0], filename.split('.')[-1]
    milis = int(round(time.time()))
    filename = "%s_%s.%s" % (name, str(milis), ext)
    return 'club/docs/{0}/{1}'.format(instance.club.id, filename)


def file_club_thumbnail(instance, filename):
    name, ext = filename.split('.')[0], filename.split('.')[-1]
    milis = int(round(time.time()))
    filename = "thumbnail_%s_%s.%s" % (name, str(milis), ext)
    return 'club/docs/{0}/thumnail/{1}'.format(instance.club.id, filename)


def file_member(instance, filename):
    ext = filename.split('.')[-1]
    milis = int(round(time.time()))
    filename = "user_%s_%s.%s" % (str(instance.user.id), str(milis), ext)
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'city'
        ordering = ['id']


class Club(models.Model):
    name = models.CharField(max_length=100)
    register_number = models.CharField(max_length=100, blank=True, null=True)
    since = models.CharField(max_length=100, blank=True, null=True)
    secretariat = models.TextField(blank=True, null=True)
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='clubs', blank=True, null=True)
    leader = models.CharField(max_length=100, blank=True, null=True)
    slogan = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to="club/logo",
                             null=True,
                             blank=True,
                             help_text="Upload Logo klub"
                             )

    class Meta:
        db_table = 'club'
        ordering = ['register_number']

    def __str__(self):
        return self.name


class SocialAccount(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    club = models.ForeignKey(
        Club, on_delete=models.CASCADE, related_name='socials')

    class Meta:
        db_table = 'social'

    def __str__(self):
        return self.name


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    club = models.ForeignKey(
        Club, on_delete=models.CASCADE, related_name='members')
    adress = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=15, blank=True, null=True)
    born_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    draw_length = models.CharField(max_length=5, blank=True, null=True)
    position = models.CharField(max_length=25, blank=True, null=True)
    picture = models.ImageField(upload_to=file_profile,
                                null=True,
                                blank=True,
                                help_text="Upload Potomu sebagai gambar profile",
                                default='user/avatar.png'
                                )

    class Meta:
        db_table = 'member'

    def __str__(self):
        return self.name


class ClubFiles(models.Model):
    uploaded = models.DateTimeField(auto_now=True, auto_now_add=False)
    club = models.ForeignKey(
        Club, on_delete=models.CASCADE, related_name='clubfiles')
    file = models.FileField(upload_to=file_club)
    filename = models.CharField(max_length=30, default=None)
    file_ext = models.CharField(max_length=30, default=None)
    mimetype = models.CharField(max_length=30, default=None)

    class Meta:
        db_table = 'club_files'

    def __str__(self):
        return self.file.name


class MemberFiles(models.Model):
    uploaded = models.DateTimeField(auto_now=True, auto_now_add=False)
    file = models.FileField(upload_to=file_member)

    class Meta:
        db_table = 'member_files'

    def __str__(self):
        return self.name
