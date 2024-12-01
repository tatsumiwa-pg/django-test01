from django.shortcuts import render
from django.views import View

class SampleView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app_folder/top.html')
top = SampleView.as_view()