from django.contrib import admin
from polls.models import Poll, Choice
# Register your models here.
class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question']
    inlines = [ChoiceInLine]
admin.site.register(Poll, PollAdmin)