from django.contrib import admin
from .models import Task,Category



# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','owner','description',)


admin.site.register(Category,CategoryAdmin)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name','priority','status')


admin.site.register(Task)
