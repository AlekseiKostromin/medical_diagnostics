from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin,
                                        UserPassesTestMixin)
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView, TemplateView)

from .forms import LabTestForm, TestCategoryForm, DoctorForm, BookingForm
from .models import TestCategory, LabTest, Doctor, Booking


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')

        send_mail(
            name,
            message,
            phone_number,
            ['olga@noran.ru'],

        )
    context = {
        'title': 'Контакты',
    }

    return render(request, 'main/contacts.html', context)


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # all_specials = Specials.objects.filter(active=True)
        # context['all_specials'] = all_specials
        return context


class LabTestListView(ListView):
    model = LabTest

    def get_queryset(self):
        labtests = LabTest.objects.all()
        return labtests


class LabTestDetailView(DetailView):
    model = LabTest
    # cart_labtest_form = CartAddProductForm


class LabTestCreateView(CreateView):
    model = LabTest
    form_class = LabTestForm
    success_url = reverse_lazy('main:index')


class LabTestUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = LabTest
    form_class = LabTestForm
    success_url = reverse_lazy('main:index')

    def test_func(self):
        user = self.request.user

        if user.is_staff or user.is_superuser:
            return True
        else:
            return False


class LabTestDeleteView(LoginRequiredMixin,
                        DeleteView):
    model = LabTest
    success_url = reverse_lazy('main:index')


class TestCategoryListView(ListView):
    model = TestCategory


class TestCategoryDetailView(DetailView):
    model = TestCategory


class TestCategoryCreateView(CreateView):
    model = TestCategory
    form_class = TestCategoryForm
    success_url = reverse_lazy('main:index')


class TestCategoryUpdateView(LoginRequiredMixin,
                             UserPassesTestMixin,
                             UpdateView):
    model = TestCategory
    form_class = TestCategoryForm
    success_url = reverse_lazy('main:index')

    def test_func(self):
        user = self.request.user

        if user.is_staff or user.is_superuser:
            return True
        else:
            return False


class TestCategoryDeleteView(LoginRequiredMixin,
                             PermissionRequiredMixin,
                             DeleteView):
    model = TestCategory
    success_url = reverse_lazy('main:index')


class DoctorListView(ListView):
    model = Doctor


class DoctorDetailView(DetailView):
    model = Doctor


class DoctorCreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy('main:index')


class DoctorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy('main:index')

    def test_func(self):
        user = self.request.user

        if user.is_staff or user.is_superuser:
            return True
        else:
            return False


class DoctorDeleteView(LoginRequiredMixin,
                       PermissionRequiredMixin,
                       DeleteView):
    model = TestCategory
    success_url = reverse_lazy('main:index')
    permission_required = 'main.delete_testcategory'


class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.patient = self.request.user
        self.object.save()

        return super().form_valid(form)
