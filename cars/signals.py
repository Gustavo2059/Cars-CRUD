from django.db.models.signals import pre_save, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from .models import Car, CarInventory, CarConfiguration
from openai_api.client import car_ai_bio


def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value = Sum('value')
    )['total_value']
    # aggregate() é um método que cria um campo personalizado, nesse caso total_value, que é a soma de todos os valores dos carros.
    
    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    # instance is the object that is being saved.
    # sender is the model class (car) that is sending the signal.
    if not instance.bio:
        try:
            enable_car_ai_bio = CarConfiguration.objects.first().enable_car_ai_bio
            
            if enable_car_ai_bio == 1:
                ai_bio = car_ai_bio(
                    instance.model,
                    instance.brand,
                    instance.model_year,
                )
                instance.bio = ai_bio
                if not ai_bio:
                    instance.bio = 'Biografia automática não disponível.'

        except AttributeError:
            instance.bio = 'Biografia automática não habilitada.'

@receiver(post_save, sender=Car)
# Indica quando a função deve ser executada e qual o modelo.
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):    
    car_inventory_update()
