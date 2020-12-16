from django.contrib import admin
from aljoadmin.models import Aljoadmin, Comment

# Register your models here.
@admin.register(Aljoadmin)
class AljoadminAdmin(admin.ModelAdmin):
    list_display = ('id', 'foodname', 'recipe', 'brand', 'tag_list', 'modify_dt')
    prepopulated_fields = {'slug': ('foodname',)}

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tags.all())

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'writer', 'content')