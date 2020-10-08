from django.db import models

import random
import string
import uuid

# Create your models here.
class UserSession(models.Model):
	get_id_user = str(uuid.uuid4())
	ID_user = models.CharField(primary_key=True, default=get_id_user, max_length=50, editable=False)
	ID_room = models.ManyToManyField('ConfRoom')
	# add encoder and decoder json?

class ConfRoom(models.Model):
	get_id_room = lambda: ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
	ID_room = models.CharField(primary_key=True, default=get_id_room(), max_length=20, editable=True)
	wait_status = models.BooleanField(default=True)
	open_status = models.BooleanField(default=True)
	time_out = models.IntegerField(default=3600) #age cookies in seconds
	#private = models.BooleanField(default=False) Method for set connect to room with secret_key'''

	def room_wait_status(self):
		pass

	def room_open_status(self):
		pass