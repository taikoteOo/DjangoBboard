from django.urls import path
from b_board.views import index, about, read_ad, add_ad


app_name = 'b_board'
urlpatterns = [
    # path('about/contacts', about, name='about'),
    # path('about/', about, name='about'), #Более специфические маршруты выше, чем более общие
    path('ad/<int:pk>/', read_ad, name='read_ad'),
    path('ad/', add_ad, name='add_ad'),
    path('', index, name='index'),
]