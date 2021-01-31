from django.contrib import admin
from .models import Account, HairProfile
from common.models import model_app
from common.utils import get_model

# Register your models here.
# admin.site.register(Account)
# admin.site.register(HairProfile)

for i in model_app:
    model = get_model(i)
    admin.site.register(model)


admin.autodiscover()
admin.site.enable_nav_sidebar = False
