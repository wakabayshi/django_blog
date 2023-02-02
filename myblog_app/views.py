from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse #追加
from .models import Post

# Create your views here.
def index(request):
    # return HttpResponse('Hello World')
    posts = Post.objects.order_by('-published')
    one = Post.objects.get(id = 1)
    two = Post.objects.get(id = 2)
    three = Post.objects.get(id = 3)
    
    params = {
        'posts': posts, 
        'one': one,
        'two': two,
        'three': three,
    }
    return render(request, 'myblog_app/index.html', params)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'myblog_app/post_detail.html', {'post':post})
    

