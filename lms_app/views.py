from django.shortcuts import render
from . models import*
from . forms import BookForm, CategoryForm

def index(request):

    if request.method == 'POST':

        addCat = CategoryForm(request.POST)
        if addCat.is_valid():
            addCat.save()

        addBook = BookForm(request.POST, request.FILES)
        if addBook.is_valid():
            addBook.save()




    context = {
        'books': Book.objects.all(),
        'category': Category.objects.all(),
        'form': BookForm(),
        'categoryForm': CategoryForm()
    }
    return render(request, 'pages/index.html', context)

def books(request):
    context = {
        'category': Category.objects.all(),
        'books': Book.objects.all(),
    }
    return render(request, 'pages/books.html', context)

