from django.contrib import admin

from hosted_app.models import HostedApp


# Register your models here.
@admin.register(HostedApp)
class AppAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'title', 'description', 'docker_container_id', 'status', 'created_at', 'updated_at', 'started_at'
    )
    list_filter = ('status',)
    ordering = ('user', 'pk',)
    list_per_page = 10
    search_fields = ('user__username', 'title')
    list_display_links = ('user', 'title')