from django.contrib import admin
from base.models import humidity
from base.models import temperature
from base.models import graphic

# Register your models here.

admin.site.register(temperature)
admin.site.register(humidity)
admin.site.register(graphic)
