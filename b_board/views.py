from django.shortcuts import render

from .forms import AdForm
from .models import Ad

def index(request):
    ad = Ad.objects.all()
    context = {'title': 'Главная страница', 'ad': ad}
    return render(request, template_name='b_board/index.html', context=context)

def about(request):
    context = {'title': 'О сайте'}
    return render(request, template_name='b_board/about.html', context=context)

def add_ad(request):
    if request.method == 'GET':
        ad_form = AdForm()
        context = {'form': ad_form, 'title': 'Добавить объявление'}
        return render(request, template_name='b_board/ad_add.html', context=context)
    if request.method == 'POST':
        ad_form = AdForm(data = request.POST)
        if ad_form.is_valid():
            post = Ad()
            post.title = ad_form.cleaned_data['title']
            post.text = ad_form.cleaned_data['text']
            post.author = ad_form.cleaned_data['author']
            post.type = ad_form.cleaned_data['type']
            post.price = ad_form.cleaned_data['price']
            post.save()
            return index(request)

def read_ad(request, pk):
    ad = Ad.objects.get(pk=pk)
    context = {'ad': ad, 'title': ad.title}
    return render(request, template_name='b_board/ad_detail.html', context=context)