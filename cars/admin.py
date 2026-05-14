from django.contrib import admin
from cars.models import Car, Brand, CarInventory, CarConfiguration

class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name',)
    search_fields = ('brand_name',)


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'value', 'plate')
    #liss_display indica os campos que serão exibidos na lista de objetos no admin.
    search_fields = ('model', "brand") 
    #Quais campos serão pesquisáveis na barra de pesquisa do admin.

class CarInventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cars_count', 'cars_value', 'created_at')
    search_fields = ('cars_count', 'cars_value')

class CarConfigurationAdmin(admin.ModelAdmin):
    list_display = ('enable_car_ai_bio',)
    search_fields = ('enable_car_ai_bio',)

admin.site.register(Car, CarAdmin)
# Esta função registra o modelo Car com a interface de administração do Django, usando a configuração definida na classe CarAdmin.
admin.site.register(Brand, BrandAdmin)
admin.site.register(CarInventory, CarInventoryAdmin)
admin.site.register(CarConfiguration, CarConfigurationAdmin)