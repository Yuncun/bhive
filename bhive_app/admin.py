from django.contrib import admin

from bhive_app.models import Answer, Question


admin.site.register(Question)
admin.site.register(Answer)