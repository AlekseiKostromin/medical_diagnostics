import random
import string

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse

from django.views.generic import CreateView, UpdateView, DetailView

from users.forms import UserRegisterForm, UserForm
from users.models import User


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    #def form_valid(self, form):
    #    self.object = form.save()
    #    self.object.save()
    #    return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserDetailView(DetailView):
    model = User

    def get_object(self, queryset=None):
        return self.request.user


@login_required
def generate_password(request):
    new_password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    request.user.set_password(new_password)
    request.user.save()
    send_mail(
        subject='Поступил запрос на смену пароля',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email],
    )
    return redirect(reverse_lazy('users:login'))
