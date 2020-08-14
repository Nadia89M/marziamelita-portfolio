from django.shortcuts import render, get_object_or_404
from .models import Category, Subcategory
from photos.models import Photo

# Create your views here.
def categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'categories/categories.html', context)

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    subcategories = Subcategory.objects.filter(category=category)
    return render(request, 'categories/view_category.html', {
        'category': category,
        'subcategories': subcategories
    })

def view_subcategory(request, slug, subslug):
    category = get_object_or_404(Category, slug=slug)
    subcategory = get_object_or_404(Subcategory, slug=subslug)
    photos = Photo.objects.filter(subcategory=subcategory).order_by('id').reverse()
    return render(request, 'categories/view_subcategory.html', {
        'category': category,
        'subcategory': subcategory,
        'photos': photos
    })