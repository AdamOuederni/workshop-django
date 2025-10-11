from django.contrib import admin
from .models import User
# Register your models here.
#admin.site.register(User)
@admin.register(User)
class AdminUserModel(admin.ModelAdmin):
    list_display=("full_name","email","role","nationality","created_at")
    ordering=("last_name",)
    list_filter=("role",)
    search_fields=("first_name","last_name")
    #fieldsets=("informations générales",{"fields":("first_name","last_name","role","affiliation","nationality")}),("Contact Info",{"fields":("email",)})
    fieldsets = (
        ("Informations générales", {
            "fields": ("user_id","first_name", "last_name", "role", "affiliation", "nationality")
        }),
        ("Contact Info", {
            "fields": ("email",)
        }),
    )
    def full_name(self, obj):
        if obj.first_name and obj.last_name:
            return f"{obj.first_name} {obj.last_name}"
        return "RAS"
    full_name.short_description = "Nom complet"
    date_hierarchy = "created_at"
    readonly_fields=("user_id",)
    list_display_links = ("email","full_name")

