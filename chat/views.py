from django.shortcuts import render
from chat.models import ChatUser
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

import datetime
import hashlib

def index(request):
	return render(request, 'index.html')

def signup(request):
	return render(request, 'signup.html')

def aboutus(request):
	return render(request, 'aboutus.html')

def signupenter(request):
	email = request.POST['email']
	username = request.POST['username']
	firstname = request.POST['firstname']
	lastname = request.POST['lastname']
	password = request.POST['password']
	gender = request.POST['gender']

	password2 = password.encode('utf-8')
	password_md5 = (hashlib.md5(password2).hexdigest())

	emailencoded = email.encode('utf-8')
	confirm_code = (hashlib.md5(emailencoded).hexdigest())

	newuser = ChatUser.objects.create(email=email, username=username, firstname=firstname, lastname=lastname, gender=gender, confirm_code=confirm_code, password=password_md5)
	newuser.save()

	# body = 'Hi ' + email + '. Please confirm your Vapr account by clicking the link here: http://www.vaporcht.com/confirm/' + confirm_code
	# send_mail('Confirm your Vapr account', body, 'admin@vaporcht.com', [email], fail_silently=False)

	return HttpResponseRedirect(reverse('signupsuccess'))

def signupsuccess(request):
	return render(request, 'signupsuccess.html')

def confirm(request, confirm_code):
	getuserbyconfirmcode = ChatUser.objects.get(confirm_code=confirm_code)
	getuserbyconfirmcode.confirm_code = 0
	getuserbyconfirmcode.confirmed = 1
	getuserbyconfirmcode.save()

	return render(request, 'confirmed.html')

def login(request):
	username = request.POST['username']
	password = request.POST['password']

	password2 = password.encode('utf-8')
	password_md5 = (hashlib.md5(password2).hexdigest())

	try:
		account = ChatUser.objects.get(username=username, password=password_md5)
		return HttpResponse("Logged in.")
	except ChatUser.DoesNotExist:
		account = None
		return HttpResponse("Error")