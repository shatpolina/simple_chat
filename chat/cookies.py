import random
import string
from . models import UserSession, ConfRoom
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.sessions.models import Session

def set_cookies():
	new_user = UserSession(ID_user = UserSession.get_id_user)
	new_user.save()
	print("Set cookies")
	#redirect to home

def check_room():
	try:
		s = Session.objects.get()
		s = s.get_decoded()
		if ConfRoom.objects.filter(ID_room = s['ID_room']):
			print('your room:', s['ID_room'])
		else:
			print('NE TA ROOM', s['ID_room'])
	except:
		print("Err from room")

def check_cookies(name_func):
	try:
		s = Session.objects.get()
		s = s.get_decoded()
		#без декодикорования принимаем редирект на чат, с декодированием просто проверяем наличие куки(принимать в функицию аргумент decoded true/false)
		print('PRINT SESSION from ' + name_func + ': ID_user = ', s['ID_user'], ", ID_room = ", s['ID_room'])
		if UserSession.objects.filter(ID_user = s['ID_user']):
			print ("Hello user")
		else:
			set_cookies()
	except:
		print("ERROR")
		set_cookies()