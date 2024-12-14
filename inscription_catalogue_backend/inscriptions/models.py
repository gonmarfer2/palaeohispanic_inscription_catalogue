from django.db import models
from django.utils.translation import gettext_lazy as _

class Medium(models.Model):
    name = models.CharField(max_length=512,verbose_name='soporte')
    
    def __str__(self):
        return self.name
    
class WritingScript(models.Model):
    name = models.CharField(max_length=512,verbose_name='signario')

    def __str__(self):
        return self.name

class Inscription(models.Model):
    class Material(models.TextChoices):
        BRONZE = "BRONCE", _("BRONCE")
        BRASS = "LATÓN", _("LATÓN")
        COPPER = "COBRE", _("COBRE")
        IRON = "HIERRO", _("HIERRO")
        POTTERY = "CERAMICA", _("CERÁMICA")
        STONE = "PIEDRA", _("PIEDRA")
        SILVER = "PLATA", _("PLATA")
        LEAD = "PLOMO", _("PLOMO")
    class WritingDirection(models.TextChoices):
        BOUSTROPHEDON = "BUSTROFEDON", _("BUSTROFEDON")
        DEXTROTARY = "DEXTROGIRA", _("DEXTROGIRA")
        LEVOROTATORY = "LEVOGIRA", _("LEVOGIRA")
        SPIRAL = "ESPIRAL", _("ESPIRAL")
    class DualSystem(models.TextChoices):
        DUAL = "DUAL", _("DUAL")
        NA = "NO APLICA", _("NO APLICA")
        NONDUAL = "NO DUAL", _("NO DUAL")

    site = models.CharField(max_length=512,blank=True,null=True,verbose_name='yacimiento')
    refMLH = models.CharField(max_length=128,verbose_name='refMLH')
    refHesperia = models.CharField(max_length=128,verbose_name='refHesperia')
    text = models.TextField(verbose_name='texto')
    town = models.CharField(max_length=512,verbose_name='municipio')
    province = models.CharField(max_length=512,verbose_name='provincia')
    material = models.CharField(max_length=64,choices=Material,default=None,null=True,verbose_name='material')
    medium = models.ForeignKey(Medium,models.SET_NULL,null=True,verbose_name='soporte')
    writing_script = models.ForeignKey(WritingScript,models.SET_NULL,null=True,verbose_name='signario')
    writing_direction = models.CharField(max_length=64,choices=WritingDirection,default=None,null=True,verbose_name='direccion_escritura')
    dual_system = models.CharField(max_length=64,choices=DualSystem,default=DualSystem.NA,verbose_name='sistema_dual')

    def __str__(self):
        return self.refHesperia

class InscriptionPhoto(models.Model):
    image = models.ImageField(verbose_name='imagen',upload_to='assets/img/')
    inscription = models.ForeignKey(Inscription,models.CASCADE,verbose_name='inscripción')

    def __str__(self):
        return self.image.name