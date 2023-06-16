
from django.urls import path, include
# from myapp.api.views import movie_details, movie_list
from myapp.api.views import MovieDetailAV, MovieListAV
urlpatterns = [

    path('list/', MovieListAV.as_view(), name='movie_list'),
    path('<int:pk>', MovieDetailAV.as_view(), name='movie_details'),
]
