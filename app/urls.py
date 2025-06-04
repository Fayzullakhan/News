from django.urls import path
from .views import home,page_404,blog_single,blog,contact,gallery_single,gallery,index,index_2
from .views import life_style,login,register,sport,technology,author
from . import views

urlpatterns = [
    path("",home,name = "home"),
    path("404/",page_404,name = "404"),
    path("author/",author,name = "author"),
    path("blog_single/",blog_single,name = "blog"),
    path("blog/",blog,name = "blog"),
    path("404/",page_404,name = "404"),
    path("contact/",contact,name = "contact"),
    path("gallery_single/",gallery_single,name = "gallery_single"),
    path("gallery/",gallery,name = "gallery"),
    path("404/",page_404,name = "404"),
    path("index_2/",index_2,name = "index_2"),
    path("index/",index,name = "index"),
    path("life_style/",life_style,name = "life_style"),
    path("login/",login,name = "login"),
    path("register/",register,name = "register"),
    path("sport/",sport,name = "sport"),
    path("technology/",technology,name = "technology"),
    path('index/', views.index, name='index'),
    path('index_dark/', views.index_dark, name='index_dark'),
    path('sport/', views.sport, name='sport'),
    path('blog/', views.blog, name='blog'),
    path('blog_single/', views.blog_single, name='blog_single'),
    
]
