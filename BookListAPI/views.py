from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse
from .models import Books
from django.http import QueryDict
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def books(request):
    if request.method == 'GET':
        books = list(Books.objects.all().values())
        return JsonResponse({'books': books})
    
    elif request.method == 'POST':
        request_body = json.loads(request.body)
        print(request_body.get('title'))
        try:
            
            title = request_body.get('title')
            author = request_body.get('author')
            price = request_body.get('price')
            inventory = 100
        
            # book = Books.objects.create(title=title, author=author, price=price, inventory=inventory)
            book = Books(title=title, author=author, price=price, inventory=inventory)
            book.save()
            return JsonResponse(model_to_dict(book))
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'}, status=400)
    
            