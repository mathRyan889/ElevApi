from django.db import models
from django.contrib.auth.models import User
from elevator.models import Elevator


class ProviderCompany(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome da Empresa")
    cnpj = models.CharField(max_length=20, unique=True, verbose_name="CNPJ")
    tel = models.CharField(max_length=20, verbose_name="Telefone")

    class Meta:
        verbose_name = "Empresa Prestadora"
        verbose_name_plural = "Empresas Prestadoras"

    def __str__(self):
        return self.name


class Maintenance(models.Model):

    class Status(models.TextChoices):
        AGENDADA = 'agendada', 'Agendada'
        EM_ANDAMENTO = 'em_andamento', 'Em Andamento'
        CONCLUIDA = 'concluida', 'Concluída'
        CANCELADA = 'cancelada', 'Cancelada'

    class Type(models.TextChoices):
        PREVENTIVA = 'preventiva', 'Preventiva'
        CORRETIVA = 'corretiva', 'Corretiva'
        EMERGENCIAL = 'emergencial', 'Emergencial'
        INSPECAO = 'inspecao', 'Inspeção'

    elevator = models.ForeignKey(
        Elevator,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        verbose_name="Elevador"
    )

    type = models.CharField(
        max_length=20,
        choices=Type.choices,
        null=False,
        blank=False,
        verbose_name="Tipo de Manutenção"
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Descrição"
    )

    responsible_technician = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        verbose_name="Técnico Responsável"
    )

    provider_company = models.ForeignKey(
        ProviderCompany,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="Empresa Prestadora"
    )

    start_date = models.DateField(
        null=False,
        blank=False,
        verbose_name="Data de Início"
    )

    end_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de Conclusão"
    )

    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Custo"
    )

    replaced_parts = models.TextField(
        null=True,
        blank=True,
        verbose_name="Peças Substituídas"
    )

    next_maintenance_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data da Próxima Manutenção"
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        null=False,
        blank=False,
        verbose_name="Status"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Manutenção"
        verbose_name_plural = "Manutenções"

        def __str__(self):
            return f"Manutenção {self.id} - {self.elevator.model} - {self.get_status_display()}"
