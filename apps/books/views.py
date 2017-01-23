from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import IntegrityError

from..login.models import User
from .models import Book, Review
from .forms import BookForm, ReviewForm

def get_user(request):
    return get_object_or_404(User, id=request.session['user']['id'])

def index(request):
    featured_reviews = Review.objects.all()[:3].prefetch_related('book')
    books = Book.objects.all()

    return render(request, 'books/index.html', {'featured_reviews':featured_reviews, 'books': books})

def new(request):
    book_form = BookForm()
    review_form = ReviewForm()
    return render(request, 'books/new.html', {'book_form': book_form, 'review_form': review_form})

def create(request):
    if request.method == 'POST':
        book_form = BookForm({'title': request.POST['title'], 'author': request.POST['author']})
        review_form = ReviewForm({'rating': request.POST['rating'], 'review': request.POST['review']})
        if book_form.is_valid() and review_form.is_valid():
            book = book_form.save()
            review_object = review_form.save(commit=False)
            review_object.book = book
            review_object.user = get_user(request)
            review_object.save()
            messages.success(request, "Book and review have been created")
            return redirect('books:show', id=book.id)
        else:
            messages.error(request, "All fields to be filled in")
            return redirect('books:new')
    else:
        return redirect('books:index')

def show(request, id):
    book = get_object_or_404(Book, id=id)
    review_form = ReviewForm()
    return render(request, 'books/show.html', {'book': book, 'review_form': review_form})

def update(request, id):
    if request.method == 'POST':
        try:
            book = Book.objects.get(id=id)
        except ObjectDoesNotExist:
            messages.error(request, 'Book does not exist')
        else:
            review_form = ReviewForm(data=request.POST)
            print review_form.is_valid()
            if review_form.is_valid():
                review_object = review_form.save(commit=False)
                review_object.book = book
                review_object.user = get_user(request)
                try:
                    review_object.save()
                except IntegrityError:
                    messages.error(request, 'You have aready reviewed this book')
                    return redirect('books:show', id=book.id)
                messages.success(request, 'Review created')
            else:
                messages.error(request, "Review needs all fields to be filled in")
    return redirect('books:show', id=book.id)


def delete(request, id):
    review = Review.objects.get(id=id)
    if request.session['user']['id'] != review.user.id:
        messages.error(request, 'You cannot delete this user\'s comment')
        return redirect('books:show', id=review.book.id)
    try:
        review.delete()
        messages.success(request, 'Review deleted')
    except ObjectDoesNotExist:
        messages.error(request, 'Review does not exist')
    return redirect('books:show', id=review.book.id)
