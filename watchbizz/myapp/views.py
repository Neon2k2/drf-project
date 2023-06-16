# from django.shortcuts import render
# from myapp.models import Movie
# # Create your views here.
# from django.http import JsonResponse


# def movie_list(request):
#     movie_list = Movie.objects.all()

#     data = {'movies': list(movie_list.values())}

#     return JsonResponse(data)


# def movie_details(request, pk):

#     movie = Movie.objects.get(pk=pk)

#     data = {'name': movie.name,
#             'description': movie.description,
#             'active': movie.active
#             }

#     return JsonResponse(data)
