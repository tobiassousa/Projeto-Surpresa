from django.urls import path
from . import views

urlpatterns = [
    path('', views.criar_convidado, name="criar_convidado"),
    path('deletar_convidado/<int:id>', views.deletar_convidado, name="deletar_convidado"),
    path('atualizar_convidado/<int:id>', views.atualizar_convidado, name="atualizar_convidado"),
]

