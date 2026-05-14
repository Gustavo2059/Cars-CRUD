from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import NewCarCreateView, CarsListView, CarDetailView, CarUpdateView, CarDeleteView
from accounts.views import register_view, login_view, logout_view


urlpatterns = [
    path('admin/', admin.site.urls),   
    # O primeiro parâmetro da função path é a URL que você deseja mapear, no caso 'admin/'.
    # O segundo parâmetro é a view que deve ser chamada quando essa URL é acessada, aqui é admin.site.urls,
    # que é a interface administrativa padrão do Django.

    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('cars/', CarsListView.as_view(), name='cars_list'),
    # Método as_view() converte a classe CarsView em uma view que pode ser usada nas URLs.
    path('new_car/', NewCarCreateView.as_view(), name='new_car'),
    # O atributo name define um nome para a URL, que pode ser usado em templates e redirecionamentos.
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'), 
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 


 