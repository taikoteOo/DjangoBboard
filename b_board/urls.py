from django.urls import path
from b_board.views import index, about, read_ad, add_ad, not_found, update_ad,delete_ad


app_name = 'b_board'
urlpatterns = [
    # path('about/contacts', about, name='about'),
    # path('about/', about, name='about'), #Более специфические маршруты выше, чем более общие
    path('ad/<slug:slug>/delete/', delete_ad, name='delete_ad'),
    path('ad/<slug:slug>/edit/', update_ad, name='update_ad'),
    path('ad/<slug:slug>/', read_ad, name='read_ad'),
    path('ad/', add_ad, name='add_ad'),
    path('404', not_found, name='404'),
    path('', index, name='index'),
]