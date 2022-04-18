from django.contrib import admin

from .models import EvaluateIndex, EvaluateLog, Student, Teacher, Sclass, Subject, EvaluateItem

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Sclass)
admin.site.register(EvaluateLog)
admin.site.register(Subject)
admin.site.register(EvaluateIndex)
admin.site.register(EvaluateItem)