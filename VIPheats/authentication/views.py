# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import View, TemplateView, FormView, RedirectView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User

from django.contrib.auth import logout, authenticate, login

from random import randint


# Create your views here.


class Index(RedirectView):
	"""
	Redirect to /vip-heats/home.
	"""
	def get_redirect_url(self, *args, **kwargs):
		user = self.request.user.is_authenticated()
		if user:
			url = '/vip-heats/home'
		else:
			url = '/login'
		return url


class SignUpUser(View):
	def get(self, request):
		ctx = {}
		ctx['rand'] = randint(100, 999)
		return render(request, 'signup.html', ctx)
	def post(self, request):
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		confirmpassword = request.POST.get('confirmpassword')
		if password == confirmpassword:
			user = User.objects.create_user(username=username,email=email, password=password)
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/vip-heats/home')
			else:
			# An inactive account was used - no logging in!
				return HttpResponse("Your  account is disabled.")
		else:
			return render(request,'signup.html',{'message':'password and confirm password does not match'})
		return render(request,'signup.html')


class LoginUser(View):
	def get(self, request):
		ctx = {}
		ctx['rand'] = randint(100, 999)
		return render(request, 'login.html', ctx)
	def post(self,request):
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				if request.user.is_superuser:
					return HttpResponseRedirect('/superadmin')
				else:
					return HttpResponseRedirect('/vip-heats/home')
		else:
			return render(request, 'login.html', {'message': 'Invalid credentials'})


class LogOut(View):
	def get(self,request):
		logout(request)
		return HttpResponseRedirect('/login') 



