from django.urls import path  
from .views import article_list, article_detail, article_create, article_edit  

urlpatterns = [  
    path('', article_list, name='article_list'),  
    path('article/<int:article_id>/', article_detail, name='article_detail'),  
    path('article/new/', article_create, name='article_create'),  
    path('article/edit/<int:article_id>/', article_edit, name='article_edit'),  
]