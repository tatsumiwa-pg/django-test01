from django.shortcuts import render, redirect, reverse
from django.views import View

class Index(View):
    def get(self, request: dict, *args, **kwargs):
        return redirect(reverse('app_folder:top'))
index = Index.as_view()