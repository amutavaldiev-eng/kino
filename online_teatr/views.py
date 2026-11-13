from django.shortcuts import render, redirect
from django.db.models import Q
from .models import *


def create_movie(request):
    genres = Genre.objects.all()
    if request.method == 'POST' and request.POST.get('name') and request.FILES.get('image'):
        Movie.objects.create(
            name=request.POST.get('name'),
            caption=request.POST.get('caption'),
            image=request.FILES.get('image'),
            genre=Genre.objects.get(id=request.POST.get('genre')))
        return redirect('movie_list')
    return render(request, 'create_movie.html', {'genres': genres})


def update_movie(request, id):
    movie = Movie.objects.get(id=id)
    genres = Genre.objects.all()
    if request.method == 'POST':
        movie.name = request.POST.get('name')
        movie.caption = request.POST.get('caption')
        movie.genre_id = request.POST.get('genre')
        movie.image = request.FILES.get('image', movie.image)
        movie.save()
        return redirect('movie_list')
    return render(request, 'update_movie.html', {'movie': movie,'genres': genres})


def delete_movie(request, id):
    movie = Movie.objects.get(id=id)
    if request.method == 'POST':
        movie.delete()
    return redirect('movie_list')


def movie_list(request):
    query = request.GET.get('q','')
    movies = Movie.objects.filter(
        Q(name__icontains=query) | Q(genre__name__icontains=query))
    return render(request, 'movies.html', {'movies': movies,'query': query})



def genres(request):
    genres = Genre.objects.all()
    return render(request, 'genres.html', {'genres': genres})


def genre_movies(request, id):
    genre = Genre.objects.get(id=id)
    movies = Movie.objects.filter(genre=genre)
    return render(request, 'genre_movies.html', {'genre': genre,'movies': movies})



def movie_detail(request, id):
    movie = Movie.objects.get(id=id)
    comments = Comment.objects.filter(movie=movie)
    return render(request, 'movie_detail.html', {'movie': movie,'comments': comments})



def add_comment(request, id):
    movie = Movie.objects.get(id=id)
    if request.method == 'POST':
        Comment.objects.create(
            username=request.POST.get('username'),
            text=request.POST.get('text'),
            movie=movie)
        return redirect('movie_detail', id=movie.id)
    return render(request, 'add_comment.html', {'movie': movie})


def my_comments(request):
    username = request.GET.get('username')
    comments = Comment.objects.filter(username=username)
    return render(request, 'my_comments.html', {'comments': comments})


def create_genre(request):
    if request.method == 'POST':
        Genre.objects.create(
            name=request.POST.get('name'))
        return redirect('genres')
    return render(request, 'create_genre.html')