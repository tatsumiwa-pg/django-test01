from django.shortcuts import render
from django.views import View
from .models import Memo

class SampleView(View):
    def get(self, request, *args, **kwargs):
        result = Memo.objects.all()
        context ={'result':result}
        return render(request, 'app_folder/top.html', context=context,)
top = SampleView.as_view()