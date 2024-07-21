from django.contrib import admin
from .models import SpecialService, Team, Skill , Category , Option , Service , Comment

class SpecialServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter  = ['status']
    search_fields = ['title']


admin.site.register(SpecialService, SpecialServiceAdmin)
admin.site.register(Team)
admin.site.register(Skill)
admin.site.register(Category)
admin.site.register(Option)
admin.site.register(Service)
admin.site.register(Comment)