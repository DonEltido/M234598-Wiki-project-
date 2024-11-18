from django.shortcuts import render, get_object_or_404, redirect  
from .models import Article  
from .forms import ArticleForm  

def article_list(request):  
    articles = Article.objects.all()  
    return render(request, 'article_list.html', {'articles': articles})  

def article_detail(request, article_id):  
    article = get_object_or_404(Article, id=article_id)  
    return render(request, 'article_detail.html', {'article': article})  

def article_create(request):  
    if request.method == "POST":  
        form = ArticleForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('article_list')  
    else:  
        form = ArticleForm()  
    return render(request, 'article_form.html', {'form': form})  

def article_edit(request, article_id):  
    article = get_object_or_404(Article, id=article_id)  
    if request.method == "POST":  
        form = ArticleForm(request.POST, instance=article)  
        if form.is_valid():  
            form.save()  
            return redirect('article_detail', article_id=article.id)  
    else:  
        form = ArticleForm(instance=article)  
    return render(request, 'article_form.html', {'form': form})