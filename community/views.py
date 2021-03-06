from django.shortcuts import render, redirect
from .models import Review

# Create your views here.

def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'community/review_list.html', context)

def new_review(request):
    return render(request, 'community/new_review.html')


def create_review(request):
    review = Review()
    review.title = request.GET.get('title')
    review.content = request.GET.get('content')
    review.rank = request.GET.get('rank')
    review.save()
    
    return redirect('/community/')


def review_detail(request, pk):
    review = Review.objects.get(id=pk)
    context = {
        'review':review
    }
    return render(request,'community/review_detail.html', context)


def delete_review(request, pk):
    review = Review.objects.get(id=pk)
    review.delete()
    return redirect('/community/')


def update_review(request, pk):
    review = Review.objects.get(id=pk)
    review.title = request.GET.get('title')
    review.content = request.GET.get('content')
    review.save()

    return redirect('/community/')

def search(request):
    keyword = request.GET.get('keyword')
    results = Review.objects.filter(title__icontains=keyword)
    context = {
        'results': results,
        'keyword': keyword,
    }

    return render(request,'community/search_result.html',context)