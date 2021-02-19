from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# from .models import Post
# from django.core.paginator import Paginator, EmptyPage
# from django.template import RequestContext
from .models import Post, Category
from django.conf import settings
from django.views.generic import ListView, CreateView
from .forms import PostForm
from django.urls import reverse_lazy
from django.db.models import Q

def get_queryset(request): 
    if request.method== "POST":
        query = request.POST.get('search_posts')
        print(query)
        return Post.objects.filter(
            Q(title__icontains=query))
    return Post.objects.all()  
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_page(request):
     username = request.POST.get('username')
     password = request.POST.get('password')
     user = authenticate(request, username=username, password=password)

    
     if user is not None:
        login(request, user)
        
        return redirect('/homepage')    
     else:  
        if request.method == "POST":
            context = { 'message': 'Please login with right credentials' }
            return render(request, 'login.html',context= context )       
        return render(request, 'login.html')       


def home_page(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    all_posts =  get_queryset(request);
    return render(request,'homepage.html', {'posts' : all_posts })
class home(ListView):
    model = Post, Category
    template_name = 'home.html'
class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('homepage')
    
# # Add new blog
# def add_new_post(request):
#     submitted = False

#     if request.method == 'POST':
#         form = PostForm(request.POST)
        
#         if form.is_valid():
#              form.save()
#              return redirect('/add_new_post/?submitted=True')
#     else:
#         form = PostForm()
#         if 'submitted' in request.GET:
#              submitted = True 
#     return render(request, 'templates/add_new_post.html', {'form': form, 'submitted': submitted})
def edit(request, id):  
    post = Post.objects.get(id=id)  
    return render(request,'templates/edit.html', {'post':post})  
def update(request, id):  
    post = Post.objects.get(id=id)  
    form = PostForm(request.POST, instance = post)  
    if form.is_valid():  
        form.save()  
        return redirect("/home")  
    return render(request, 'templates/edit.html', {'post': post, 'form': form})  
def destroy(request, id):  
    post = Post.objects.get(id=id)  
    post.delete()  
    return redirect("/home") 
 

# def getPost(request):
#     # Get specified post
#     post = Post.objects.filter().order_by('-created_on')
#     context = {
#         "posts": posts,
#     }

#     # Display specified post
#     return render(request,'single.html', context)

# def getCategory(request, selected_page=1):
#     # Get specified category
#     posts = Post.objects.all().order_by('-created_on')
#     category_posts = []
#     for post in posts:
#         if post.categories.filter():
#             category_posts.append(post)

#     # Add pagination
#     pages = Paginator(category_posts, 5)

#     # Get the category
#     category = Category.objects.filter()[0]

#     # Get the specified page
#     try:
#         returned_page = pages.page(selected_page)
#     except EmptyPage:
#         returned_page = pages.page(pages.num_pages)

#     # Display all the posts
#     return render(request,'category.html', { 'posts': returned_page.object_list, 'page': returned_page, 'category': category})

# class PostsFeed():
#     title = "Blog Posts"
#     link = "feeds/posts/"
#     description = "Posts from My Blog"

#     def items(self):
#         return Post.objects.order_by('-created_on')[:5]

#     def item_title(self, item):
#         return item.title

#     def item_description(self, item):
#         return item.text