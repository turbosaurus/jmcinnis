from django.contrib import admin
from mezzanine.core.admin import StackedDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from portfolio.models import ProjectPage, Category, ProjectImage


class ProjectImageInline(StackedDynamicInlineAdmin):
    model = ProjectImage


class ProjectPageAdmin(PageAdmin):
    inlines = [ProjectImageInline]

admin.site.register(ProjectPage, ProjectPageAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)