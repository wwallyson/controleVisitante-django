from django.db import models

# Create your models here.
class Morador(models.Model):
    cpf = models.CharField(verbose_name='CPF', max_length=11)
    nome_completo = models.CharField(verbose_name="Nome Completo", max_length=200)
    numero_app = models.CharField(verbose_name="numero app", max_length=11)
  
    class Meta:
        verbose_name = "Morador"
        verbose_name_plural = "Moradores"
        db_table = "Morador"
    
    def __str__(self) -> str:
        return self.nome_completo