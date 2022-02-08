from django.contrib import admin

from main.models import CodeImage, Problema, Comment, Reply


class ImageInline(admin.TabularInline):
    model = CodeImage
    min_num = 1
    max_num = 5


@admin.register(Problema)
class ProblemAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Reply)
admin.site.register(Comment)