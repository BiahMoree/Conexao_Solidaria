from django.db import models

class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    data_de_nascimento = models.DateField()
    usuario = models.CharField(max_length=50, unique=True)
    senha = models.CharField(max_length=128)

    def str(self):
        return self.nome