from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.contrib import messages

from .forms import CustomUserCreationForm

User = get_user_model()


def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:home')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=user.email, password=raw_password)
            # login(request, user)
            messages.success(request,f'Your account has been created, you\'re now able to log in.')
            return redirect('users:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form, 'title': 'Sign-Up'})


class Profile(DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'user'
    slug_field = 'slug'
    slug_url_kwarg = 'user'
    query_pk_and_slug = True

    def get_queryset(self, **kwargs):
        return User.objects.get(pk=self.kwargs['pk'])

    def get_object(self, **kwargs):
        return User.objects.get(pk=self.kwargs['pk'])