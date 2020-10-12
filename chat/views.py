import random
import string
import uuid
from . models import UserSession, ConfRoom
from . import cookies
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.sessions.models import Session

new_room = UserSession

# Create your views here.
def index(request):
	cookies.check_cookies(request, 'chat')

	return render(request, 'chat/index.html')

def new_room(request):
	cookies.check_cookies(request, 'new_room')
	ID_user = request.session['ID_user']

	user = UserSession.objects.get(pk = ID_user)
	new_room = ConfRoom.objects.create(ID_room = ConfRoom.get_id_room(), wait_status = True)
	user.ID_room.add(new_room)

	print('GOSPOGA PROVERKA:', new_room.ID_room)

	request.session['ID_room'] = new_room.ID_room

	return redirect('/chat/' + new_room.ID_room + '/')

def random_room(request):
	cookies.check_cookies(request, 'random_room')
	ID_user = request.session['ID_user']

	user = UserSession.objects.get(pk = ID_user)
	try:
		room = ConfRoom.objects.values_list('ID_room', flat=True).filter(wait_status = True).first()
		random_room = ConfRoom.objects.get(pk = room)
		ConfRoom.objects.filter(pk = room).update(wait_status = False)
		# !!! Как сделать чтобы к одному юзеру не привязывалось второй раз?!
		user.ID_room.add(random_room)

		request.session['ID_room'] = random_room.ID_room
	except:
		print('ALL CHATS ARE BUSY')
		return redirect('/chat/')
	
	return redirect('/chat/' + room + '/')


def room(request, room_name):
	cookies.check_cookies(request, 'room')

	if cookies.check_room(request, room_name):
		return render(request, 'chat/room.html', {
			'room_name': room_name
		})
	else:
		return redirect('/chat/')

'''def private_room(request, room_name):
	# Private room with password to acceess
	cookies.check_cookies('user_room', True)
	#get and set name and password for room
	# get users setings and add it in list settings from class ConfRoom
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

#add method
#			  Exit() - clean id_room in cookies after user escape room
#			  Clean_cookies() - clean all expired session every day (and data) (filter db)