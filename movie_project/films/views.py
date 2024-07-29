from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'films/add_movie.html', {'form': form})

def edit_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'films/edit_movie.html', {'form': form, 'movie': movie})

def movie_list(request):
    movies = Movie.objects.all().order_by('title')
    return render(request, 'films/movie_list.html', {'movies': movies})
