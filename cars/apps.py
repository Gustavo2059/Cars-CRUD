from django.apps import AppConfig


class CarsConfig(AppConfig):
    name = 'cars'

    def ready(self):
        # Garante que quando a app "cars" for inicializada, os sinais definidos em cars.signals sejam importados e registrados.
        import cars.signals

