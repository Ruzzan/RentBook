from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Book, Comment
from .forms import UploadBookForm, CommentForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def Home(request):
    books = Book.objects.all()
    context = {
        'books':books
    }
    return render(request, 'Book/home.html', context)

def UserBooks(request):
    books = Book.objects.filter(manager = request.user)
    return render(request, 'Book/userbook.html', {'books':books})

def Detail(request, book_slug):
    book = Book.objects.get(slug = book_slug)
    comments = Comment.objects.filter(book = book).order_by('id')

    # comment form to add comment in books 
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            content = request.POST.get('content')
            Comment.objects.create(book=book, manager = request.user , content = content)
            messages.success(request, 'Your comment has been added.')
    else:
        comment_form = CommentForm()

    context = {
        'book':book, 
        'comments':comments,
        'comment_form':comment_form
    }

    return render(request, 'Book/detail.html',context)

def DeleteComment(request, id):
    comment = get_object_or_404(Comment, id=id).delete()
    messages.success(request, 'Your Comment has been deleted.')
    return reverse('home')
    


@login_required
def AddBook(request):
    if request.method == 'POST':
        form = UploadBookForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit = False)
            instance.manager = request.user
            instance.save()
            messages.success(request, 'Book was successfully added.')
            return redirect('home')
    else:
        form = UploadBookForm()
    return render(request, 'Book/add.html', {'form':form})

@login_required
def EditBook(request,slug):
    book = get_object_or_404(Book, slug=slug)
    if request.method == 'POST':
        form = UploadBookForm(request.POST, request.FILES, instance = book)

        if form.is_valid():
            form.save()
            messages.success(request, 'Book was successfully edited.')
            return redirect('mybooks')
    else:
        form = UploadBookForm(instance = book)
    return render(request, 'Book/edit.html', {'form':form, 'book':book})

def DeleteBook(request, slug):
    book = get_object_or_404(Book, slug = slug)
    book.delete()
    messages.success(request, 'Book was successfully deleted.')
    return redirect('mybooks')

def Search(request):
    search_term = request.GET['search_term']
    search_results = Book.objects.filter(
        Q(name__icontains = search_term) |
        Q(author__icontains = search_term) |
        Q(location__icontains = search_term) |
        Q(category__icontains = search_term)
    )
    context = {
        'search_term':search_term,
        'books':search_results,
    }
    return render(request, 'Book/search.html', context)


def add_variable_to_context(request):
    book = Book.objects.filter(manager = request.user)
    comment = Comment.objects.filter(book = book)

    return {
        'books': book,
        'comments':comment
    }






