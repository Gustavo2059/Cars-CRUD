from django import forms
from cars.models import Car

class CarModelForm(forms.ModelForm):
    # Formulário baseado no modelo Car.
    class Meta: 
        model = Car
        fields = "__all__"  # Inclui todos os campos do modelo Car no formulário.

    def clean_value(self):
        # No Django, os métodos de limpeza personalizados devem ser nomeados como 'clean_<fieldname>'.
        value = self.cleaned_data.get("value")
        # Captura o valor do campo "Value" do formulário enviado pelo usuário.
        # cleaned_data é uma função nativa do django que retorna um dicionário com os dados validados do formulário.
        if value < 10000:
            self.add_error("value", "O valor do carro não pode ser menor que R$10.000,00")
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get("factory_year")
        if factory_year < 1975:
            self.add_error("factory_year", "O ano de fabricação não pode ser antes que 1975")
        return factory_year
        
        
      