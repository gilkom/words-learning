from django.contrib import admin
from nauka.models import User
from nauka.models import Word
from nauka.models import Learning

# Register your models here.
admin.site.register(User)
admin.site.register(Word)
admin.site.register(Learning)