from django.db import models
from django.contrib.auth.models import User


class Manufacturer(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True)

    cnpj = models.CharField(
        max_length=20,
        unique=True,
        null=False,
        blank=False,
        verbose_name="CNPJ")

    tel = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name="Telefone"
    )

    class Meta:
        ordering = ['name']
        verbose_name = "Fabricante"
        verbose_name_plural = "Fabricantes"

    def __str__(self):
        return self.name


class Elevator(models.Model):

    class Status(models.TextChoices):
        OPERACIONAL = 'operacional', 'Operacional'
        EM_MANUTENCAO = 'em_manutencao', 'Em Manutenção'
        INATIVO = 'inativo', 'Inativo'

    serial_number = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False,
        verbose_name="Número de Serie")

    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        verbose_name="Fabricante"
    )

    model = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Modelo"
    )

    capacity_kg = models.IntegerField(
        null=False,
        blank=False,
        verbose_name="Capacidade em kg"
    )

    num_floors = models.IntegerField(
        null=False,
        blank=False,
        verbose_name="Número de Andares"
    )

    installation_location = models.TextField(
        null=False,
        blank=False,
        verbose_name="Local de Instalação"
    )

    installation_date = models.DateField(
        null=False,
        blank=False,
        verbose_name="Data de Instalação"
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.OPERACIONAL
    )

    responsible_technician = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="Técnico Responsável"
    )

    observations = models.TextField(
        null=True,
        blank=True,
        verbose_name="Observações"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Elevador"
        verbose_name_plural = "Elevadores"

    def __str__(self):
        return f"{self.serial_number} - {self.manufacturer} {self.model}"
