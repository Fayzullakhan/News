from django.shortcuts import render


# # views.py
# from datetime import datetime
# # from django.shortcuts import render

# def my_view(request):
#     today = datetime.now().strftime("%A, %B %d, %Y")
#     return render(request, 'index_dark.html', {'today': today})



def home(request):
    return render(request,'index.html')
def page_404(request):
    return render(request,'404.html')
def author(request):
    return render(request,'author.html')
def blog_single(request):
    return render(request,'blog_single.html')
def blog(request):
    return render(request,'blog.html')
def contact(request):
    return render(request,'contact.html')
def gallery_single(request):
    return render(request,'gallery_single.html')
def gallery(request):
    return render(request,'gallery.html')
def index_2(request):
    return render(request,'index_2.html')
def index(request):
    return render(request,'index.html')
def life_style(request):
    return render(request,'life_style.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def sport(request):
    return render(request,'sport.html')
def technology(request):
    return render(request,'technology.html')
def custom_404(request, exception):
    return render(request, '404.html', status=404)
def index_dark(request):
    return render(request,'index_dark.html')