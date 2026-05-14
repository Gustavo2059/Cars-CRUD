from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=200)

    def __str__(self):
        return self.brand_name
    
    
class Car(models.Model):
    #Nome desta classe será o nome da tabela no banco de dados.
    #Ela herda de models.Model, que é a classe base para todos os modelos do Django.
    
    id = models.AutoField(primary_key=True)
    #Campo id é uma chave primária auto-incrementada do banco de dados. É um método herdado de models.Model.
    
    model = models.CharField(max_length=200)
    #O método CharField cria um campo de texto com tamanho máximo definido pelo parâmetro max_length. 
    #blank=True permite que o campo seja criado em branco, 
    #e null=True permite que o campo armazene valores nulos no banco de dados.
    
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="car_brand")
    #Tipo de campo que liga a tabela "brand"
    #"on_delete=models.PROTECT" impede a exclusão de uma marca se houver carros associados a ela. Se "on_delete=models.CASCADE" fosse usado, excluir uma marca também excluiria todos os carros associados a ela.
    #"related_name" define o nome da relação.

    factory_year = models.IntegerField(blank=True, null=True)
    #O método IntegerField cria um campo que armazena números inteiros.
    
    model_year = models.IntegerField(blank=True, null=True)

    plate = models.CharField(max_length=7, blank=True, null=True)
    
    value = models.FloatField(blank=True, null=False)
    #O método FloatField cria um campo que armazena números de ponto flutuante

    photo = models.ImageField(upload_to='car_photos/', blank=False, null=False)
    #Toda foto que o usuário fizer upload será salva na pasta 'car_photos/' dentro do diretório de mídia configurado no projeto Django. 

    bio = models.TextField(blank=True, null=True, max_length=250)

    def __str__(self):
        #Este é um método padrão de Models do Django que define a representação em string da classe na página Admin.
        return f'{self.brand} - {self.model} ({self.model_year})'
    
class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    # O método auto_now_add=True define que o campo created_at será 
    # preenchido automaticamente com a data e hora atuais quando um 
    # novo registro for criado.
    class Meta:
        ordering = ['-created_at']
        # A opção ordering define a ordem padrão dos registros quando eles são consultados via query.
    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'
    
class CarConfiguration(models.Model):
    # Classe destinada a configurações do sistema de gerenciamento de carros.

    enable_car_ai_bio = models.IntegerField(
        default=False,
        verbose_name='Habilitar biografia automática (IA) de carros?',)
    
    def __str__ (self):
        return f'Configurações do sistema de gerenciamento de carros'