from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import Group,User
from django.utils.html import format_html
from admin_export_action.admin import export_selected_objects
# from admin_interface.models import Theme
from .models import *
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.models import Attachment
# Register your models here.

class BlogAdmin(SummernoteModelAdmin,admin.ModelAdmin):
    list_display = ('description' ,'is_enabled', 'image_tag' , 'name','category','change', 'delete',)
    search_fields = ['name']
    
    actions = ['enable_selected', 'disable_selected',export_selected_objects,]
    summernote_fields=('description',)


    def image_tag(self,obj):
        return obj.image_tag
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    def change(self, obj):
        return format_html('<a class="btn" href="/admin/trapsi/blog/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn" href="/admin/trapsi/blog/{}/delete/">Delete</a>', obj.id)

    def enable_selected(self,request,queryset):
        queryset.update(is_enabled=True)
    
    def disable_selected(self,request,queryset):
        queryset.update(is_enabled=False)

    
admin.site.register(Blog , BlogAdmin)

class RegistrationApplicationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name','city',]
    list_filter = ('date','course')
    list_display = ('name', 'mobileno' ,'course', 'email', 'date','change', 'delete',)
    actions =[export_selected_objects,]
    def change(self, obj):
        return format_html('<a class="btn" href="/admin/trapsi/registrationapplication/{}/change/">Change</a>', obj.id)
    
    
    def delete(self, obj):
        return format_html('<a class="btn" href="/admin/trapsi/registrationapplication/{}/delete/">Delete</a>', obj.id)
admin.site.register(RegistrationApplication , RegistrationApplicationAdmin)

class EnquireAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name_or_company']
    # list_filter = ('process')
    list_display = ('name_or_company', 'date' ,'mobileno', 'service', 'qutation_cost','process','change', 'delete',)
    actions =[export_selected_objects,]
    def change(self, obj):
        return format_html('<a class="btn" href="/admin/trapsi/enquire/{}/change/">Change</a>', obj.id)
    
    
    def delete(self, obj):
        return format_html('<a class="btn" href="/admin/trapsi/enquire/{}/delete/">Delete</a>', obj.id)
admin.site.register(Enquire , EnquireAdmin)

class ClientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name_or_company']
    # list_filter = ('process')
    list_display = ('name_or_company', 'date' ,'mobileno', 'service', 'start_date', 'End_date', 'account_details','payment','change', 'delete',)
    actions =[export_selected_objects,]
    def change(self, obj):
        return format_html('<a class="btn" href="/admin/trapsi/client/{}/change/">Change</a>', obj.id)
    
    
    def delete(self, obj):
        return format_html('<a class="btn" href="/admin/trapsi/client/{}/delete/">Delete</a>', obj.id)
admin.site.register(Client , ClientAdmin)

class ClientFormAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name','company']
    # list_filter = ('process')
    list_display = ('name', 'company' ,'mobileno', 'email', 'intrest', 'subject', 'date','change', 'delete',)
    actions =[export_selected_objects,]
    def change(self, obj):
        return format_html('<a class="btn" href="/admin/trapsi/clientform/{}/change/">Change</a>', obj.id)
    
    
    def delete(self, obj):
        return format_html('<a class="btn" href="/admin/trapsi/clientform/{}/delete/">Delete</a>', obj.id)
admin.site.register(ClientForm , ClientFormAdmin)

# admin.site.register(Theme)
admin.site.site_title="LOGIN TrapsiBytes"
admin.site.site_header="TrapsiBytes"
admin.site.index_title="TrapsiBytes Backend Portal"