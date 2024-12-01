from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

class Index(View):
    def get(self, request, *args, **kwargs):
        return redirect(reverse('app_folder:top'))
index = Index.as_view()