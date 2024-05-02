from django.urls import path, include
from .views import ArtistAPIView, SongsAPIView, SongDetailAPIView, AlbomAPIViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('alboms', viewset=AlbomAPIViewSet)


urlpatterns = [
    path("artists/", ArtistAPIView.as_view(), name="artist"),
    path("", include(router.urls)),
    path("songs/", SongsAPIView.as_view(), name="songs"),
    path("songs/<int:id>/", SongDetailAPIView.as_view(), name="song-detail")
]