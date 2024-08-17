from django.shortcuts import render
from .models import Post
from django.utils import Timezone

def Post_list(request):
    posts = Post.objects.filter(Published_date__lte = Timezone.now()).order_by('Published_date')
    return render(request,'blog/post_list.html', {'posts': posts})