from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('books/', views.BooksPage.as_view(), name='books'),
    path('contacts/', views.ContactsPage.as_view(), name='contacts'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('books/science/atom/', views.AtomPage.as_view(), name='atom'),
    path('books/science/biology/', views.BiologyPage.as_view(), name='biology'),
    path('books/economics/', views.EconomicsPage.as_view(), name='economics'),
    path('books/science/', views.SciencePage.as_view(), name='science'),
    path('books/science/biology/bio-tech/', views.BioTechPage.as_view(), name='bio-tech'),
    path('books/programming/', views.ProgrammingPage.as_view(), name='programming'),
    path('books/science/biology/bio-tech/news/', views.NewsPage.as_view(), name='news'),

]