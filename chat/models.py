from django.db import models

import random
import string

# Create your models here.
class UserSession(models.Model):
	ID_user = models.CharField(primary_key=True, max_length=50, editable=False)
	ID_room = models.ManyToManyField('ConfRoom')

class ConfRoom(models.Model):
	get_id_room = lambda: ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
	ID_room = models.CharField(primary_key=True, max_length=20, editable=True)
	wait_status = models.BooleanField()
	open_status = models.BooleanField(default=True)
	time_out = models.IntegerField(default=3600)
	#private = models.BooleanField(default=False) Method for set connect to room with secret_key'''

	def room_wait_status(self):
		pass

	def room_open_status(self):
		pass