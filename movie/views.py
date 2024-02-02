# movie/views.py
from django.shortcuts import render
from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer

class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def list(self, request, *args, **kwargs):
        movies = self.get_queryset()
        return render(request, 'movie/movie_list.html', {'movies': movies})

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return render(request, 'movie/movie_detail.html', {'movie': instance})
