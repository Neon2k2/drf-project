
from django.urls import path, include
# from myapp.api.views import movie_details, movie_list
from myapp.api.views import WatchDetailAV, WatchListAV
from myapp.api.views import StreamPlatformAV
from myapp.api.views import StreamPlatformDetailAV
urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name="streamplatform-detail")

]
