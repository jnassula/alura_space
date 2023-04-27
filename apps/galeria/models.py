from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALAXIA', 'Galaxia'),
        ('PLANETA', 'Planeta'),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(
        max_length=100, choices=OPCOES_CATEGORIA, default=''
    )
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    publicada = models.BooleanField(default=True)
    data_fotografia = models.DateTimeField(default=datetime.now)
    usuario = models.ForeignKey(
        User,
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f'Fotografia [ nome={self.nome} ]'
