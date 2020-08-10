
from django.urls import path
from . import views
app_name ="articles"
urlpatterns = [
    path('',views.articles_list, name='list'),
    path('article_create',views.article_create, name ='create'),
    path('<slug:slug>',views.article_detail, name ='detail'),
]
