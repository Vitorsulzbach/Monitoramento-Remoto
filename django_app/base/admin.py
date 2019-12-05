from django.contrib import admin
from base.models import humidity
from base.models import temperature
from base.models import graphic
from base.models import globalvar
from base.models import longgraphic

# Register your models here.

admin.site.register(temperature)
admin.site.register(humidity)
admin.site.register(graphic)
admin.site.register(globalvar)
admin.site.register(longgraphic)
