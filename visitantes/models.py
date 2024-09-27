from django.db import models

class Visitante(models.Model):
    STATUS_VISITANTE = [
        ('AGUARDANDO', 'aguardando autorização'),
        ('EM_VISITA', 'Em visita'),
        ('FINALIZADO', 'Visita Finalizada')
    ]
    
    status = models.CharField(verbose_name='status', max_length=10, choices=STATUS_VISITANTE, default='AGUARDANDO')
    nome_completo = models.CharField(verbose_name='nome completo', max_length=200)
    cpf = models.CharField(verbose_name='cpf', max_length=11)
    telefone = models.CharField(verbose_name='telefone', max_length=11)
    data_de_nascimento = models.DateField(verbose_name='data de nascimento')
    numero_casa = models.PositiveSmallIntegerField(verbose_name='número da casa a ser visitada')
    placa_veiculo = models.CharField(verbose_name='placa do veículo', max_length=7, blank=True, null=True)
    horario_chegada = models.DateTimeField(verbose_name='Horário de chegada na portaria', auto_now_add=True)
    horario_autorizacao = models.DateTimeField(verbose_name='Horário de autorização na portaria', auto_now_add=True, null=True)
    horario_saida = models.DateTimeField(verbose_name='Horário de saída na portaria', blank=True, null=True)
    morador_responsavel = models.CharField(verbose_name='nome do morador responsável', max_length=200)
    registrado_por = models.ForeignKey('porteiros.Porteiro', verbose_name='porteiro responsável', on_delete=models.PROTECT)

    def get_horario_saida(self):
        return self.horario_saida

    def get_horario_autorizacao(self):
        return self.horario_autorizacao

    def get_cpf(self):
        if self.cpf:
            cpf = str(self.cpf)
            cpf_formatado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
            return cpf_formatado

    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        db_table = 'visitante'

    def __str__(self):
        return self.nome_completo
