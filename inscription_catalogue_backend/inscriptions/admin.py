from django.contrib import admin
from inscriptions.models import *

# Register your models here.
class InscriptionAdmin(admin.ModelAdmin):
    pass
class InscriptionPhotoAdmin(admin.ModelAdmin):
    pass
class MediumAdmin(admin.ModelAdmin):
    pass
class WritingScriptAdmin(admin.ModelAdmin):
    pass

admin.site.register(Inscription,InscriptionAdmin)
admin.site.register(InscriptionPhoto,InscriptionAdmin)
admin.site.register(Medium,MediumAdmin)
admin.site.register(WritingScript,WritingScriptAdmin)