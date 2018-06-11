from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class IndexPage(TemplateView):
    template_name = 'index.html'


class ContactsPage(TemplateView):
    template_name = 'contacts.html'


class AtomPage(TemplateView):
    template_name = 'atom.html'


class AboutPage(TemplateView):
    template_name = 'about.html'


class BiologyPage(TemplateView):
    template_name = 'biology.html'


class EconomicsPage(TemplateView):
    template_name = 'economics.html'


class SciencePage(TemplateView):
    template_name = 'science.html'


class BioTechPage(TemplateView):
    template_name = 'bio_tech.html'


class BooksPage(TemplateView):
    template_name = 'books.html'


class ProgrammingPage(TemplateView):
    template_name = 'programming.html'


class NewsPage(TemplateView):
    template_name = 'news.html'
