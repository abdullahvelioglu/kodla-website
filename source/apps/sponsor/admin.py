# Third-Party
from adminsortable.admin import SortableAdmin

# Django
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Local Django
from sponsor.models import SponsorType, Sponsor


@admin.register(SponsorType)
class SponsorTypeAdmin(SortableAdmin):
    readonly_fields = ('create_date', 'update_date')
    list_display = ('name', 'description', 'is_active')
    list_filter = ('is_active', 'create_date', 'update_date')
    list_editable = ('is_active',)
    search_fields = ('name',)


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    fields = (
        ('name', 'url'), ('logo', 'logo_prev'), ('logo_height', 'logo_width'),
        ('create_date', 'update_date'), 'is_active'
    )
    readonly_fields = ('create_date', 'update_date', 'logo_prev')
    list_display = (
        'name', 'url', 'logo_height', 'logo_width', 'logo_prev', 'is_active'
    )
    list_filter = ('is_active', 'create_date', 'update_date')
    list_editable = ('logo_height', 'logo_width', 'is_active')
    search_fields = ('name',)
