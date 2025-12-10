from django.contrib import admin

from .models import User, Topic, Room, Message

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)

class TopicAdmin(admin.ModelAdmin):
    pass

admin.site.register(Topic, TopicAdmin)


class RoomAdmin(admin.ModelAdmin):
    pass

admin.site.register(Room, RoomAdmin)


class MessageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Message, MessageAdmin)
