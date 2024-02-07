from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True )
    last_modified = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/Post/', blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['-date_posted']

class Event(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True )
    last_modified = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/Event/', blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['-date_posted']

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True )
    last_modified = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/Announcement/', blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('announcement-detail', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['-date_posted']

class About(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    about_date = models.DateTimeField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True )
    last_modified = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/About/', blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('about-detail', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['-date_posted']

# home page text
class Home1(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True )
    last_modified = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/Home1/', blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('home-detail', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['-date_posted']

class Home2(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True )
    last_modified = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/Home2/', blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('home-detail', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['-date_posted']

class Home3(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True )
    last_modified = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/Home3/', blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('home-detail', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['-date_posted']

class Member(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    pronouns = models.CharField(max_length=100, blank=True, null=True)
    insta = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='images/Member/', blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    archive = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('member-detail', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['name']

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True )
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['-date_posted']


class InstagramPost(models.Model):
    thumbnail_url = models.URLField(max_length=500, blank=True, default='')
    caption = models.TextField()

    def __str__(self):
        return self.caption