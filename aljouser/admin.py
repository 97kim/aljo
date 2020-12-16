from django.contrib import admin
from aljouser.models import Aljouser, CommentUser

# Register your models here.
@admin.register(Aljouser)
class AljouserAdmin(admin.ModelAdmin):
    list_display = ('id', 'foodname', 'recipe', 'brand', 'role', 'tag_list', 'modify_dt')

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tags.all())

@admin.register(CommentUser)
class CommentUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'writer', 'content')