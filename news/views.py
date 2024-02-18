from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Team, News, Contact


from django.views.generic import DetailView, ListView, CreateView
from django.urls import reverse_lazy

# Create your views here.


def index(request):
    teams = Team.objects.all()
    return render(request, "index.html", {"teams": teams})


def about_us(request):
    teams = Team.objects.all()
    return render(request, "about.html", {"teams": teams})


class Blog(ListView):
    model = News
    template_name = "blog.html"


class DetailBlog(DetailView):
    template_name = "blog-single.html"
    model = News


class CreateNewsView(CreateView):
    template_name = "createnews.html"
    model = News
    fields = ["category", "title", "text", "images"]
    success_url = reverse_lazy("blog")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CreateTeamView(CreateView):
    template_name = "createteam.html"
    model = Team
    fields = ['name', 'image', 'title']
    success_url = reverse_lazy('home')

class ContactView(TemplateView):
    template_name = 'contact.html'

class CreateContactView(CreateView):
    template_name = "base.html"
    model = Contact
    fields = ['fullname', 'email', 'text']
    success_url = reverse_lazy('home')

