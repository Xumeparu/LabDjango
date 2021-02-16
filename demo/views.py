from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from demo.models import Book


def first(request):
    return HttpResponse('Hello, world!')


class Second(View):
    def get(self, request):
        return HttpResponse(self.output)

    books = Book.objects.all()
    output = ''

    for book in books:
        output += (f'We have {book.title} with ID {book.id} in our Database<br>')
