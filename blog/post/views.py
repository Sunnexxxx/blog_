# from django.shortcuts import render
# from django.urls import reverse, reverse_lazy
# from django.views.generic import ListView, CreateView, DetailView
#
# from post.forms import PostForm
# from post.models import Post, Category
#
#
# # Create your views here.
# def index(request):
#     return render(request, 'post/index.html')
#
#
# class PostListView(ListView):
#     model = Post
#     template_name = 'post/index.html'
#     context_object_name = 'posts'
#     paginate_by = 3
#
#     # extra_context = {
#     #     'categories': Category.objects.all(),
#     # }
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.all()
#         context['current_page'] = self.request.GET.get('page')
#         return context
#
#     def get_queryset(self):
#         posts = Post.objects.filter(category_id=1)
#         return posts
#     # page_kwarg = 'page'
#
#
# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'post/detail.html'
#     context_object_name = 'post'
#     pk_url_kwarg = 'post_id'
#
#     # def get_object(self, queryset=None):
#
#
# class PostCreateView(CreateView):
#     form_class = PostForm
#     template_name = 'post/create.html'
#     success_url = reverse_lazy('index_by_class')
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
#
#
# class PostController:
#     def all_published_posts(request):
#         posts = Post.objects.filter(is_published=True)
#         return render(request, 'all_published_posts.html', {'posts': posts})
#
#     def posts_by_category(request, category):
#         posts = Post.objects.filter(is_published=True, category=category)
#         return render(request, 'posts_by_category.html', {'posts': posts})

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from .forms import PostForm
from .models import Post, Category


class IndexView(ListView):
    template_name = 'post/index.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['current_page'] = self.request.GET.get('page')
        return context

    def get_queryset(self):
        queryset = Post.objects.filter(is_published=True)
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'


class PostCreateView(CreateView):
    form_class = PostForm
    template_name = 'post/create.html'
    success_url = reverse_lazy('index_by_class')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
