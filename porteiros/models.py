from django.db import models

# Create your models here.
class Porteiro(models.Model):
    usuario = models.OneToOneField('usuarios.Usuario', verbose_name="Usuario", on_delete=models.PROTECT)
    nome_completo = models.CharField(verbose_name="nome completo", max_length=200)
    cpf = models.CharField(verbose_name="cpf", max_length=11) 
    telefone = models.CharField(verbose_name="Telefone", max_length=11)
    data_nascimento = models.DateField(verbose_name="sua data de nascimento", auto_now=False, auto_now_add=False)
    
    class meta:
        verbose_name = "Porteiro"
        verbose_name_plural = "Porteiros"
        db_table = "porteiro"
        
    def _str_(self) -> str:
        return self.nome_completo