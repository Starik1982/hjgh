
from django.contrib import admin
from .models import *

class FaqAdmin(admin.TabularInline):
    model = Faq
    extra = 0

class FaqAdmin (admin.ModelAdmin):
    list_display = [field.name for field  in Faq._meta.fields]

    class Meta:
        model = Faq

admin.site.register(Faq, FaqAdmin)


class NewsAdmin(admin.TabularInline):
    model = News
    extra = 0

class NewsAdmin (admin.ModelAdmin):
    list_display = [field.name for field  in News._meta.fields]

    class Meta:
        model = News

admin.site.register(News, NewsAdmin)




class VideoAdmin(admin.TabularInline):
    model = News
    extra = 0

class VideoAdmin (admin.ModelAdmin):
    list_display = [field.name for field  in Video._meta.fields]

    class Meta:
        model = Video

admin.site.register(Video, VideoAdmin)

class AdsAdmin(admin.TabularInline):
    model = Ads
    extra = 0

class AdsAdmin (admin.ModelAdmin):
    list_display = ['ads'] 

    class Meta:
        model = Ads

admin.site.register(Ads, AdsAdmin)


class HiroAdmin(admin.TabularInline):
    model = Hiro
    extra = 0

class HiroAdmin (admin.ModelAdmin):
    list_display = [field.name for field  in Hiro._meta.fields] 

    class Meta:
        model = Hiro
admin.site.register(Hiro, HiroAdmin)

class TalentAdmin(admin.TabularInline):
    model = Talent
    extra = 0

class TalentAdmin (admin.ModelAdmin):
    list_display = [field.name for field  in Talent._meta.fields] 

    class Meta:
        model = Talent
admin.site.register(Talent, TalentAdmin)

