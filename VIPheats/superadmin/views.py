# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import View, TemplateView, FormView, RedirectView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.urlresolvers import reverse

from random import randint

from django.contrib.auth import logout, authenticate, login

from authentication.models import *

from .models import *

# Create your views here.

class Home(LoginRequiredMixin, TemplateView):

    """
    The base view that can list all materials for users.
    """

    login_url = '/login/'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = super(Home, self).get_context_data(**kwargs)

        user = self.request.user # Get login user

        categories = Category.objects.all()

        # Add categories if empty
        if categories.count() == 0:
        	category1 = Category(name='Men')
        	category1.save()
        	category2 = Category(name='Women')
        	category2.save()
        	category3 = Category(name='Kids')
        	category3.save()

        ctx['title'] = 'VIPHeats'
        ctx['heading'] = 'VIPHeats'
        ctx['username'] = user

        # Create a random intiger 
        ctx['rand'] = randint(100, 999)

        return ctx
'''
class Home1(View):
	def get(self, request):
		"""
		The base view for admin that can list all materials categories.
		"""
		if request.user.is_authenticated:		# Check whether the user is loged in
			themes = Theme.objects.filter(id=1)
			materials = Materials.objects.all()
			context = {}
			"""
			Adding default css to the context
			"""


				context['urls'] = []
				context['materials'] = materials

				user = self.request.user # Get login user

        		ctx['title'] = 'VIPHeats'
        		ctx['heading'] = 'VIPHeats'
        		ctx['username'] = user
				"""
				Add urls to the page header
    			"""
				context['urls'].append({'url_name': 'Logout', 'url': 'logout'})
			return render(request, 'home.html', context)
		else:
			return render(request, 'login.html')

'''

class MaterialsList(View):
	"""
	The base view for admin that can list all materials by categories.
	"""
	def get(self, request, category):
		if request.user.is_authenticated:  # Check whether the user is loged in
			themes = Theme.objects.filter(id=1)
			materials = Materials.objects.filter(category__name=category)
			context = {}
			"""
			Adding default css to the context
			"""
			for theme in themes:
				context['header_font_color'] = theme.header_font_color
				context['headerbackground_color'] = theme.header_color
				context['footerbackground_color'] = theme.footer_color

				context['urls'] = []
				context['materials'] = materials
			
				context['urls'].append({'url_name': 'Logout', 'url': 'logout'})
				if request.user.is_superuser:
					context['urls'].append({'url_name': 'Add', 'url': 'materials/add'})
					context['urls'].append({'url_name': 'Theme', 'url': 'change-theme'})
			return render(request, 'materiallist.html', context)
		else:
			return render(request, 'login.html')

class MaterialsAdd(View):
	"""
	The view for admin to add materials.
	"""
	def get(self, request):
		if request.user.is_authenticated: # Check whether the user is loged in
			return render(request, 'materials_add.html')
		else:
			return render(request, 'login.html')
	def post(self,request):
		name_of_material = request.POST.get('name_of_material')
		category = request.POST.get('category')
		price = request.POST.get('Price')
		description = request.POST.get('description')
		image = request.FILES.get('files')

		print 'category', category

		materials = Materials()
		
		materials.name = name_of_material
		materials.category=Category.objects.get(name=category)
		materials.price = price
		materials.description = description
		materials.image = image
		materials.save()

		redirect_url = reverse('superadmin-home')
		return HttpResponseRedirect(redirect_url)


