import random
import string
from . models import UserSession, ConfRoom
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.sessions.models import Session

new_room = UserSession

# Create your views here.
def index(request):
	return render(request, 'chat/index.html')

def check_cookies_content(name_func):
	s = Session.objects.get()
	sm = s.get_decoded()
	print('PRINT SESSION from ' + name_func + ':', sm)
	#чтобы писать в дб надо десериализовать

def random_room(request):
	# add checksession method
	new_room.ID_user = UserSession.get_id_user
	room_name = ConfRoom.get_id_room()
	print('GOSPOGA PROVERKA:', new_room.ID_user, room_name)
	#request.session['user_session'] = new_room
	request.session['ID_user'] = new_room.ID_user
	request.session['ID_room'] = room_name

	check_cookies_content('random_room')

	return redirect('/chat/' + room_name + '/')

def user_room(request, room_name):
	# add checksession method
	#request.session['ID_user'] = new_room.ID_user
	#request.session['ID_room'] = new_room.ID_room

	check_cookies_content('user_room')

	return render(request, 'chat/room.html', {
		'room_name': room_name
	})