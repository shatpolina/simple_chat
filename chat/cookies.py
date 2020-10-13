import random
import string
import uuid
from . models import UserSession, ConfRoom
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.sessions.models import Session

def set_cookies(request):
	ID_user = str(uuid.uuid4())
	print("SET COOKIES, ID_user: ", ID_user)
	new_user = UserSession.objects.create(ID_user = ID_user)

	request.session['ID_user'] = new_user.ID_user

def check_room(request, room_name):
	try:
		s = request.session['ID_room']
		if ConfRoom.objects.filter(ID_room = s) and s == room_name:
			print('your room:', s)
			return True
		else:
			print('NE TA ROOM', s)
			return False
	except Exception as e:
		print(e)
		return False
		print("Err from room")

def check_cookies(request, name_func):
	try:
		ID_user = request.session['ID_user']
		print('PRINT SESSION from ' + name_func + ': ID_user = ', ID_user)
		if UserSession.objects.filter(ID_user = ID_user):
			print ("Hello user")
		else:
			set_cookies(request)
	except Exception as e:
		print("ERROR from " + name_func)
		#print(e)
		set_cookies(request)