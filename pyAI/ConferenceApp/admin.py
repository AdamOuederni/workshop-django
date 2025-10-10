from django.contrib import admin
from .models import Conference,Submission,OrganizingCommittee
# Register your models here.
# admin.site.register(Conference)
admin.site.register(Submission)
admin.site.register(OrganizingCommittee)
admin.site.site_title="Gestion Conférence 25/26"
admin.site.site_header="Gestion Conférences"
admin.site.index_title="django app conférence"
class SubmissionInline(admin.TabularInline):
    model = Submission
    extra=1
    readonly_fields=("submission_date",)
    
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
        

