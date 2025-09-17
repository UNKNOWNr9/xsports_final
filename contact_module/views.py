from django.shortcuts import render
from django.views.generic import View

class ContactView(View):
    def get(self, request):
        context = {}
        return render(request, 'contact_module/contact.html', context)