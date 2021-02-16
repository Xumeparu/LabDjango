from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from demo.models import Book


def first(request):
    return HttpResponse('Hello, world!')


class Second(View):
     def get(self, request):
         return HttpResponse('Function inside class check')
#
#     books = Book.objects.all()
#     output = f'We have {len(books)} books in our Database.'
