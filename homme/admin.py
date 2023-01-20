from django.contrib import admin
from .models import Setting,Header,Skill,Team,Work,Partner,Service,Price,Characteristic,Subscribe,Message,CounterUp



class SettingAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('title','subtitle')
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title','progress')
    list_editable =["progress",]
class PartnerAdmin(admin.ModelAdmin):
    fields=('photo','admin_photo')
    list_display = ('admin_photo',)
    readonly_fields=('admin_photo',)
class TeamAdmin(admin.ModelAdmin):
    fields=('name','genre','photo','admin_photo')
    list_display = ('admin_photo','name','genre')
    readonly_fields=('admin_photo',)
class WorkAdmin(admin.ModelAdmin):
    fields=('title','subtitle','type','url','photo','admin_photo')
    list_display = ('admin_photo','title','subtitle','url')
    readonly_fields=('admin_photo',)
class ServiceAdmin(admin.ModelAdmin):
    fields=('icon','title','content')
    list_display = ('title','content')
class PriceAdmin(admin.ModelAdmin):
    fields=('icon','title','popular','service','money','characteristic')
    list_display = ('service','title','popular','money')
class CounterUpAdmin(admin.ModelAdmin):
    fields=('icon','title','count')
    list_display = ('title','count')
class MessageAdmin(admin.ModelAdmin):
    fields=('name','subject','email','message')
    list_display = ('name','subject','email')
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
# Register your models here.
admin.site.register(Setting,SettingAdmin)
admin.site.register(Header,HeaderAdmin)
admin.site.register(Skill,SkillAdmin)
admin.site.register(Team,TeamAdmin)
admin.site.register(Work,WorkAdmin)
admin.site.register(Partner,PartnerAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Price,PriceAdmin)
admin.site.register(Characteristic)
admin.site.register(Subscribe)
admin.site.register(Message,MessageAdmin)
admin.site.register(CounterUp,CounterUpAdmin)