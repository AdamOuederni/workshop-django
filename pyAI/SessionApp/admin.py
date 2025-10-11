from django.contrib import admin
from .models import Session
# Register your models here.
#admin.site.register(Session)
# Register your models here.
@admin.register(Session)
class AdminSessionModel(admin.ModelAdmin):
    list_display = ("title", "topic", "session_day", "start_time", "end_time", "room", "is_morning_session","created_at", "update_at")
    list_display_links = ("title",)
    ordering = ("session_day", "start_time")
    list_filter = ("topic", "session_day", "room")
    search_fields = ("title", "topic", "room")
    fieldsets = (
        ("Informations sur la session", {
            "fields": ("title", "topic", "room")
        }),
        ("Horaires", {
            "fields": ("session_day", "start_time", "end_time")
        }),
        ("Métadonnées", {
            "fields": ("created_at", "update_at"),
        }),
    )
    save_as = True
    save_on_top = True
    readonly_fields = ("created_at", "update_at")
    list_per_page = 15
    def is_morning_session(self, obj):
        return obj.start_time.hour < 12
    is_morning_session.short_description = "Session du matin"
    is_morning_session.boolean = True
