from django.contrib import admin
from .models import Conference,Submission,OrganizingCommittee

# Register your models here.
# admin.site.register(Conference)
admin.site.register(Submission)
# admin.site.register(OrganizingCommittee)
admin.site.site_title="Gestion Conférence 25/26"
admin.site.site_header="Gestion Conférences"
admin.site.index_title="django app conférence"
class SubmissionInline(admin.TabularInline):
    model = Submission
    extra=1
    readonly_fields=("submission_date",)

@admin.register(OrganizingCommittee)
class AdminOrganizingComitteeModel(admin.ModelAdmin):
    list_display = ("user", "conference", "committee_role", "date_joined", "created_at", "update_at")
    list_filter = ("committee_role", "conference")
    search_fields = ("user__first_name", "user__last_name", "conference__title")
    ordering = ("-created_at",)
    fieldsets = (
        ("Informations générales", {
            "fields": ("user", "conference", "committee_role", "date_joined")
        }),
        ("Suivi administratif", {
            "fields": ("created_at", "update_at"),
            "classes": ("collapse",)
        }),
    )

    readonly_fields = ("created_at", "update_at")
    def user_fullname(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    user_fullname.short_description = "Nom complet"
  

@admin.register(Conference)
class AdminConferenceModel(admin.ModelAdmin):
    list_display=("name","theme","start_date","end_date","duration")
    ordering=("start_date","end_date")
    list_filter=("theme",)
    search_fields=("name",)
    date_hierarchy="start_date"
    fieldsets=("information général",{"fields":("conference_id","name","theme","description")}),("logistics Info",{"fields":("location","start_date","end_date")})
    readonly_fields=("conference_id",)
    def duration(self,objet):
        if objet.start_date and objet.end_date:
            return (objet.end_date - objet.start_date).days
        return "RAS"
    duration.short_description="Duration (days)"
    inlines=[SubmissionInline]
    
        

