from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .models import Menu, Laundry
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.
@login_required
def home(request):
    return render(request, 'dashboard/user.html')

@login_required
def laundry(request):
    return render(request, 'dashboard/laundry.html')

class LaundryCreateView(LoginRequiredMixin, CreateView):
    model = Laundry
    fields = ['tshirt', 'jeans', 'shorts', 'bedsheet', 'towel', 'shirts', 'hoodie']

    def form_valid(self, form):
        form.instance.rollno = self.request.user.profile.rollno
        form.instance.student = self.request.user
        print(form.instance)
        return super().form_valid(form)

@login_required
def menu(request):
    breakfast = Menu.objects.get(meal="Breakfast")
    lunch = Menu.objects.get(meal="Lunch")
    dinner = Menu.objects.get(meal="Dinner")
    return render(request, 'dashboard/menu.html', context={'breakfast': breakfast, 'lunch': lunch, 'dinner': dinner})

@login_required
def canteen(request):
    return render(request, 'dashboard/nightcanteen.html')

@login_required
def clean(request):
    return render(request, 'dashboard/clean.html')