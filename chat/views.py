import random
import string
from . models import UserSession, ConfRoom
from . import cookies
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.sessions.models import Session

new_room = UserSession

# Create your views here.
def index(request):
	return render(request, 'chat/index.html')

def new_room(request):
	cookies.check_cookies('new_room')

	new_room = ConfRoom(ID_room = ConfRoom.get_id_room())
	# get users setings and add it in list settings from class ConfRoom
	# integration with private_room?
	new_room.save()

	print('GOSPOGA PROVERKA:', new_room.ID_room)

	request.session['ID_room'] = new_room.ID_room

	return redirect('/chat/' + new_room.ID_room + '/')

def room(request, room_name):
	cookies.check_cookies('room')
	cookies.check_room()

	return render(request, 'chat/room.html', {
		'room_name': room_name
	})

'''def private_room(request, room_name):
	# Private room with password to acceess
	cookies.check_cookies('user_room', True)
	#get and set name and password for room
	#redirect to room
	#wait
	return render(request, 'chat/room.html', {
		'room_name': room_name
	})'''

"""def to_room(request, room_name):
	# Access to the private room
	# Seems like private_room(), but check password
	room = ConfRoom(ID_room = room_name)
	room.save()
	#request.session['ID_room'] = room_name
	return render(request, 'chat/room.html', {
		'room_name': room_name 
		})"""

#add method random_room() for get to user wait random room
#			  Exit() - clean id_room in cookies after user escape room
#			  Clean_cookies() - clean all expired session every day (and data) (filter db)