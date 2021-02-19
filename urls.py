from django.urls import include, path
from . import views
from django.views.generic import ListView
from .models import Category, Post
from django.conf.urls import url


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'), 
    path(r'^signup/$',views.signup, name='signup'),
    url(r'^homepage$', views.home_page, name='homepage'),
    path('add-new-post', views.CreatePost, name='add-new-post'),
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy), 
    # url(r'^categories/$', ListView.as_view(model=Category)),
    # url(r'^getPost/$', views.getPost),
    # url(r'^categories/$', views.getCategory),
    

    
    
    

    # Comments
    # url(r'^comments/', include('django.contrib.comments.urls')),

    # RSS feeds
    # url(r'^feeds/posts/$', PostsFeed()),

    # Flat pages
    # url(r'', include('django.contrib.flatpages.urls')),
]
