from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .forms import NewsForm
from .models import News, Category
from django.views.generic import ListView, DetailView, CreateView


# Второй способ
class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Главная'} Не рекомендуется

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class CategoryNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


# Первый способ
# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей'
#     }
#     return render(request, 'news/index.html', context)


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     cat = Category.objects.get(pk=category_id)
#     return render(request, 'news/category.html', {'news': news, 'category': cat})

class ViewNews(DetailView):
    model = News
    template_name = 'news/view_news.html'
    context_object_name = 'news_item'
    # pk_url_kwarg = 'news_id'


# def view_news(request, news_id):
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_news.html', {"news_item": news_item})

class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home')

# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # news = News.objects.create(**form.cleaned_data) Для не связаных с моделью форм
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {"form": form})
