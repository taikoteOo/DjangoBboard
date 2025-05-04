from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import AdForm
from .models import Ad

def index(request):
    ads = Ad.objects.all()
    context = {'title': 'Главная страница', 'ads': ads}
    return render(request, template_name='b_board/index.html', context=context)

def about(request):
    context = {'title': 'О сайте'}
    return render(request, template_name='b_board/about.html', context=context)

@login_required
def add_ad(request):
    if request.method == 'GET':
        ad_form = AdForm(author=request.user)
        context = {'form': ad_form, 'title': 'Добавить объявление'}
        return render(request, template_name='b_board/ad_add.html', context=context)
    if request.method == 'POST':
        ad_form = AdForm(data = request.POST, files=request.FILES, author=request.user)
        if ad_form.is_valid():
            ad_form.save()
            return index(request)

def read_ad(request, slug):
    ad = get_object_or_404(Ad, slug=slug)
    context = {'ad': ad, 'title': ad.title}
    return render(request, template_name='b_board/ad_detail.html', context=context)

@login_required
def update_ad(request, slug):
    ad = get_object_or_404(Ad, slug=slug)
    if request.method == 'POST':
        ad_form = AdForm(data=request.POST, files=request.FILES, author=request.user)
        if ad_form.is_valid():
            ad_form.save()
            return read_ad(request, ad.slug)
    else:
        ad_form = AdForm(initial={
            'title': ad.title,
            'text': ad.text,
            'image': ad.image,
        }, author=request.user)
        return render(request, template_name='b_board/ad_edit.html', context={'form': ad_form})

@login_required
def delete_ad(request, slug):
    ad = get_object_or_404(Ad, slug=slug)
    context = {'ad':ad}
    if request.method == 'POST':
        ad.delete()
        return redirect('b_board:index')
    return render(request, template_name='b_board/ad_delete.html', context=context)

def page_not_found(request, exception):
    return render(request, template_name='b_board/404.html', context={'title':'404'})

def not_found(request):
    return render(request, template_name='b_board/404.html', context={'title': '404'})