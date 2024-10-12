from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_cards, name='image_cards'),  # Página principal com os cards
    path('show-image/', views.show_image, name='show_image'),  # Para mostrar a imagem selecionada
]
