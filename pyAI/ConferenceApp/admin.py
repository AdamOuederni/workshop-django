from django.contrib import admin
from .models import Conference,Submission,OrganizingCommittee
# Register your models here.
admin.site.register(Conference)
admin.site.register(Submission)
admin.site.register(OrganizingCommittee)
admin.site.site_title="Gestion Conférence 25/26"
admin.site.site_header="Gestion Conférences"
admin.site.index_title="django app conférence"