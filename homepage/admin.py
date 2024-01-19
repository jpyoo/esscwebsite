from django.contrib import admin
from .models import Post
from .models import Event
from .models import Announcement
from .models import About, Home1, Home2, Home3, Member, Contact, ArchiveBanners


admin.site.site_header = "ESSC Admin"
admin.site.site_title = "ESSC Admin Portal"
admin.site.index_title = "Welcome to ESSC Admin Portal"

# Register your models here.
# admin.site.register(Post)
admin.site.register(Event)
# admin.site.register(Announcement)
admin.site.register(About)
admin.site.register(Home1)
admin.site.register(Home2)
# admin.site.register(Home3)
admin.site.register(Member)
admin.site.register(Contact)
admin.site.register(ArchiveBanners)

#unable user register and permission
from django.contrib.auth.models import Group
admin.site.unregister(Group)
from django.contrib.auth.models import User
admin.site.unregister(User)
#disable password change
User.change_password = False

