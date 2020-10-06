from django.urls import path, re_path
from . import views
from . import consumers

urlpatterns = [
	path('', views.index, name='index'),
	path('random/', views.random_room),
	path('<str:room_name>/', views.user_room),
]

websocket_urlpatterns = [
	re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
]