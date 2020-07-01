# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import View

from django.contrib.auth.models import User

from django.contrib.auth import logout, authenticate, login

from django.views.generic import View, TemplateView, FormView, RedirectView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.urlresolvers import reverse

from random import randint

from authentication.models import *

from superadmin.models import Materials

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

        ctx['title'] = 'VIPHeats'
        ctx['heading'] = 'VIPHeats'
        ctx['username'] = user

        # Create a random intiger 
        ctx['rand'] = randint(100, 999)

        return ctx


class MaterialList(LoginRequiredMixin, TemplateView):

    """
    The base view that can list all materials for users.
    """

    login_url = '/login/'
    template_name = 'materiallist.html'

    def get_context_data(self, **kwargs):
        ctx = super(MaterialList, self).get_context_data(**kwargs)

        category = self.kwargs['category'] # category from url

        user = self.request.user # Get login user
        materials = Materials.objects.filter(category__name=category)

        ctx['title'] = 'VIPHeats'
        ctx['heading'] = 'VIPHeats'
        ctx['username'] = user

        ctx['materials'] = materials

        # Create a random intiger 
        ctx['rand'] = randint(100, 999)

        return ctx


