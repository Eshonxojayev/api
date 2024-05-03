from django.urls import path, include
from .views import ArtistAPIView, ArtistDetailAPIView,AlbomAPIView, AlbomDetailAPIView, SongsAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('songs', viewset=SongsAPIView)


urlpatterns = [
    path("artists/", ArtistAPIView.as_view(), name="artist"),
    path("artists/", ArtistDetailAPIView.as_view(), name="artist"),
    path("", include(router.urls)),
    path("alboms/", AlbomAPIView.as_view(), name="alboms"),
    path("alboms/<int:id>/", AlbomDetailAPIView.as_view(), name="albom-detail"),
]