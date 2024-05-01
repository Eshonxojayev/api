from django.urls import path
from .views import LandingPageAPIView, ArtistAPIView, AlbomAPIView, SongsAPIView

urlpatterns = [
    path("landing/", LandingPageAPIView.as_view(), name="landing"),
    path("artists/", ArtistAPIView.as_view(), name="artist"),
    path("alboms/", AlbomAPIView.as_view(), name="albom"),
    path("songs/", SongsAPIView.as_view(), name="songs")
]