from django.contrib import admin

from myapp.models import WatchList
from myapp.models import StreamPlatform
from myapp.models import Review



# Register your models here.

admin.site.register(WatchList)

admin.site.register(StreamPlatform)

admin.site.register(Review)