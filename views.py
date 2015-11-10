# Create your views here.
from django.template.loader import get_template

from django.http import HttpResponse
from django.shortcuts import render_to_response
from bookdb.models import Book,Author
from bookdb.forms import BookForm



def insert(request):
    if request.method == 'POST':
        book = BookForm(request.POST)
        if book.is_valid():
            cd = book.cleaned_data
            if len(Author.objects.filter(AuthorID=cd['AuthorID']))<=0:
                new_author=Author(AuthorID =cd['AuthorID'], Name =cd['Name'],\
                Age =cd['Age'],Country =cd['Country'])
                new_author.save()
                new_book=Book(ISBN=cd['ISBN'],Title=cd['Title'],AuthorID=new_author,\
                Publisher=cd['Publisher'],PublishDate=cd['PublishDate'],Price=cd['Price'])
                new_book.save()
            else:
                
                new_book=Book(ISBN=cd['ISBN'],Title=cd['Title'],AuthorID=Author.objects.get(AuthorID=cd['AuthorID']),\
                Publisher=cd['Publisher'],PublishDate=cd['PublishDate'],Price=cd['Price'])
                new_book.save()
            return render_to_response('add.html', {'form': BookForm()})
    else:
        book= BookForm()
    return render_to_response('add.html', {'form': book})

def detail(request):
    ide=request.GET["id"]
    book=Book.objects.get(ISBN=ide)
    author=book.AuthorID
    return render_to_response('book.html',{'book': book,'author': author})
    
def update(request):
    ide=request.GET["id"]
    book=Book.objects.get(ISBN=ide)
    author=book.AuthorID
    return render_to_response('update.html',{'book': book,'author': author})
def supdate(request):
    isbn=request.GET["id"]
    book=Book.objects.get(ISBN=isbn)
    author=book.AuthorID
    if request.POST:
        post=request.POST
        if post['new_Title']:
            book.Title=post['new_Title']
        if post['new_ISBN']:
            book.ISBN=post['new_ISBN']
        if post['new_date']:
            book.PublishDate=post['new_date']
        if post['new_Price']:
            book.Price=post['new_Price']
        if post['new_Publisher']:
            book.Publisher=post['new_Publisher']
        if post['new_ID']:
            author.AuthorID=post['new_ID']
        if post['new_Age']:
            author.Age=post['new_Age']
        if post['new_Name']:
            author.Name=post['new_Name']
        if post['new_Country']:
            author.Publisher=post['new_Country']
        book.save()
        author.save()
        return render_to_response('book.html',{'book': book,'author': author})
    return render_to_response('update.html',{'book': book,'author': author})

    
    
def delete(request):
    ide=request.GET["id"]
    book=Book.objects.get(ISBN=ide)
    author=book.AuthorID
    if len(Book.objects.filter(AuthorID__Name =author.Name ))<=1:
        author.delete()
    book.delete()
    return render_to_response('search.html')

    
def search_from(request):
    
    return render_to_response('search.html')


def add(request):
    return render_to_response('add.html',{'form': BookForm()})
    

def name_search(request):
    error = False
    if 'q1' in request.GET:
        q1 = request.GET['q1']
        if not q1:
            error = True
        else:
            
            books=Book.objects.filter(AuthorID__Name = q1)
            return render_to_response('search_results.html',\
           {'books': books, 'query': q1})
        
    return render_to_response('search.html',
        {'error': error})

 
