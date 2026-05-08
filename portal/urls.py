from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/<str:category>/<str:agent_id>/', views.agent_chat, name='agent_chat'),
    path('api/chat/', views.chat_api, name='chat_api'),
]
