from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Review

# Create your views here.
class ReviewListView(ListView):
    model = Review
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(ReviewListView, self).get_context_data(**kwargs)
        context['review_list'] = Review.objects.all()
        return context

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'r_r_details.html'
    fields = ['review']

class ReviewCreateView(CreateView):
    model = Review
    template_name = 'r_r_new.html'
    fields = ['eatery', 'title', 'review', 'rating', 'author']
    success_url = reverse_lazy('home')

class ReviewUpdateView(UpdateView):
    model = Review
    template_name = 'r_r_edit.html'
    fields = ['eatery', 'title', 'review', 'rating']
    success_url = reverse_lazy('home')

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'r_r_delete.html'
    success_url = reverse_lazy('home')