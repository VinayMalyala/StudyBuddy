from django.contrib import admin

from .models import Topic, Room, Message

# Register your models here.
class TopicAdmin(admin.ModelAdmin):
    pass

admin.site.register(Topic, TopicAdmin)


class RoomAdmin(admin.ModelAdmin):
    pass

admin.site.register(Room, RoomAdmin)


class MessageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Message, MessageAdmin)
