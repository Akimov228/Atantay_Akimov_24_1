from django.shortcuts import HttpResponse, render
from posts.models import Post
import datetime




def main(reguest):
    if reguest.method == 'GET':
        return render(reguest, 'layouts/index.html')

def posts_view(reguest):
    if reguest.method == 'GET':
        posts = Post.objects.all()

        context = {
            'posts': posts
        }

        return render(reguest, 'posts/posts.html',context=context)


def show_date(reguest):
    # current_date
    current_date = datetime.date.today()
    if reguest.method == 'GET':
        return HttpResponse(f'{current_date}')

