from django.contrib import admin

from .models import Expense
from .models import Income
from .models import Token

# Register your models here

admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(Token)
