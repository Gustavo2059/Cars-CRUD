from cars.models import Car
from cars.forms import CarModelForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class CarsListView(ListView): 
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        # O método get_queryset é sobrescrito para personalizar a consulta ao banco de dados.
        # super() chama o método get_queryset da classe pai (ListView) para obter a queryset padrão, que é todos os objetos do modelo Car.
        search = self.request.GET.get('search')

        if search:
            cars = cars.filter(model__icontains=search)

        return cars
    
class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    
@method_decorator(login_required(login_url='/login/'), name='dispatch')
# Decorador que encapsula essa classe, exigindo que o usuário esteja autenticado para acessar a view.
# dispatch é o método que processa a requisição HTTP e determina qual método (get, post, etc.) deve ser chamado com base no tipo de requisição.
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy ('car_detail', kwargs={'pk': self.object.pk})
        # Função que recebe parâmetros para construir a URL de redirecionamento.

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'