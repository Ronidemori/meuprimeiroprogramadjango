from django.db import models

# Crie seus modelos aqui.
class Departamento(models.Model):
    nome = models.CharField(max_length=20)
    def  _str_ (self):
        return self.nome 

class Funcionario(models.Model):
    CARGOS = [
        ('ES', 'Estagiario'),
        ('As', 'Assistente'),
        ('JR', 'Junior'),
        ('PL', 'Pleno'),
        ('SR', 'Senior'),
        ('GR', 'Gerente')
    ]    
    matricula = models.IntegerField()
    nome = models.CharField(max_length=50)
    cargo = models.CharField(max_length=2, choices = CARGOS)    
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    salario = models.DecimalField(max_digits=10,decimal_places=2)
    data_nascimento = models.DateField(null=True)
    class Meta:
        ordering = ('nome')
