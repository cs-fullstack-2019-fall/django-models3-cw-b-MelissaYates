from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Book
import datetime


def index(request):
    return HttpResponse("Hello, world.")

# Create 2 entries using 2 different methods
def addBook(request):
    book1 = Book(name="The Hunger Games", pageNumber=33, genre="Fiction", publishDate="1986-03-06")
    book2 = Book(name="The Desire of Ages", pageNumber=13, genre="Non-Fiction", publishDate="1940-06-01")
    book3 = Book(name='The Immortalists', pageNumber='23', genre='Fiction', publishDate='2018-01-09')
    book1.save()
    book2.save()
    book3.save()
    return HttpResponse("Added")


def allBook(request):
    booksList = Book.objects.all()
    for eachElement in booksList:
        print(eachElement.name)
    return HttpResponse("All books")


def allBookPublishDates(request):
    booksList = Book.objects.all()
    for eachElement in booksList:
        # print(eachElement.publishDate)
        if (eachElement.publishDate > datetime.date(2018, 1, 1)):
            print(f" Book Name: {eachElement.name} Publish Date: {eachElement.publishDate}") #prints out book that is published passed 2018/01/01
    return HttpResponse("All books")
