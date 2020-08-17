from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import ArticleModel, ImageModel, TextModel
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from itertools import chain


class HomeView(ListView):
    model = ArticleModel
    template_name = 'articles/home.html'
    context_object_name = 'objects'
    ordering = ['-date_posted']

    def get_queryset(self):
        return ArticleModel.objects.filter(publish=True)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = ArticleModel
    fields = ['title', 'cover_image', 'description', 'categories']
    template_name = 'articles/create_article.html'

    def get_success_url(self):
        user_latest_article = ArticleModel.objects.all().filter(author=self.request.user).last()
        return reverse('write', kwargs={'form_id': user_latest_article.id})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
def write_view(request, form_id):
    article = get_object_or_404(ArticleModel, pk=form_id)
    if request.user != article.author:
        return HttpResponseForbidden()
    image_formset = inlineformset_factory(ArticleModel, ImageModel, fields=('image', 'image_description', ), extra=1)
    text_formset = inlineformset_factory(ArticleModel, TextModel, fields=('header', 'text', ), extra=1)
    formset_1 = image_formset(instance=article)
    formset_2 = text_formset(instance=article)
    if request.method == 'POST':
        formset_1 = image_formset(request.POST, request.FILES, instance=article)
        formset_2 = text_formset(request.POST, instance=article)
        if formset_2.is_valid() and formset_1.is_valid():
            formset_1.save()
            formset_2.save()
            return redirect('write', form_id=form_id)
    context = {
        'article': article,
        'form_1': formset_1,
        'form_2': formset_2,
    }
    return render(request, 'articles/write.html', context)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ArticleModel
    fields = ['title', 'cover_image', 'description', 'categories']
    template_name = 'articles/edit_article.html'

    def get_success_url(self):
        article = self.get_object()
        return reverse('write', kwargs={'form_id': article.id})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ArticleModel
    template_name = 'articles/delete_article.html'
    context_object_name = 'object'
    success_url = '/'

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False


@login_required
def publish(request, form_id):
    article = get_object_or_404(ArticleModel, pk=form_id)
    if request.user != article.author:
        return HttpResponseForbidden()
    if not article.publish:
        article.publish = True
        article.save()
        messages.success(request, 'Your article has been published')
    else:
        messages.info(request, 'This article has been published already')
    return redirect('home')


class ArticleDetailView(DetailView):
    model = ArticleModel
    template_name = 'articles/detail.html'
    context_object_name = 'object'
    queryset = ArticleModel.objects.filter(publish=True)

    def sort(self):
        article = self.get_object()
        images = article.imagemodel_set.all()
        text_contents = article.textmodel_set.all()
        combine = list(chain(images, text_contents))
        for i in range(len(combine)-1):
            min_pos = i
            for j in range(i, len(combine)):
                if combine[j].timestamp < combine[min_pos].timestamp:
                    min_pos = j
            combine[i], combine[min_pos] = combine[min_pos], combine[i]
        return combine

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_content'] = self.sort()
        return context


class PreviewView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = ArticleModel
    template_name = 'articles/preview.html'
    context_object_name = 'object'

    def sort(self):
        article = self.get_object()
        images = article.imagemodel_set.all()
        text_contents = article.textmodel_set.all()
        combine = list(chain(images, text_contents))
        for i in range(len(combine)-1):
            min_pos = i
            for j in range(i, len(combine)):
                if combine[j].timestamp < combine[min_pos].timestamp:
                    min_pos = j
            combine[i], combine[min_pos] = combine[min_pos], combine[i]
        return combine

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_content'] = self.sort()
        return context

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False


class DraftView(LoginRequiredMixin, ListView):
    model = ArticleModel
    template_name = 'articles/draft.html'
    context_object_name = 'objects'
    ordering = ['-date_posted']

    def get_queryset(self):
        return ArticleModel.objects.filter(publish=False, author=self.request.user)


class CategoryView(ListView):
    model = ArticleModel
    template_name = 'articles/category.html'
    context_object_name = 'objects'
    ordering = ['-date_posted']

    def get_queryset(self):
        # return get_object_or_404(ArticleModel, publish=True, categories=self.kwargs.get('category'))
        return ArticleModel.objects.filter(publish=True, categories=self.kwargs.get('category'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs.get('category')
        return context

