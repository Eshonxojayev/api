from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist, Albom, Songs
from .serializers import ArtistSerializer, AlbomSerializer, SongsSerializer
from rest_framework import status
from rest_framework.viewsets import ModelViewSet


class ArtistAPIView(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(data=serializer.data)

class ArtistDetailAPIView(APIView):
    def get(self, request, id):
        try:
            artists = Artist.objects.get(id=id)
            serializer = AlbomSerializer(artists)
            return Response(data=serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        artists = Artist.objects.get(id=id)
        serializer = SongsSerializer(instance=artists, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        artists = Artist.objects.get(id=id)
        serializer = SongsSerializer(instance=artists, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        artists = Artist.objects.get(id=id)
        artists.delete()
        return Response(data={}, status=status.HTTP_204_NO_CONTENT)

class AlbomAPIView(APIView):
    def get(self, request):
        alboms = Albom.objects.all()
        serializer = AlbomSerializer(alboms, many=True)
        return Response(data=serializer.data)


class AlbomDetailAPIView(APIView):

    def get(self, request, id):
        try:
            albom = Albom.objects.get(id=id)
            serializer = AlbomSerializer(albom)
            return Response(data=serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def patch(self, request, id):
        albom = Albom.objects.get(id=id)
        serializer = SongsSerializer(instance=albom, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, id):
        albom = Albom.objects.get(id=id)
        serializer = SongsSerializer(instance=albom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        albom = Albom.objects.get(id=id)
        albom.delete()
        return Response(data={}, status=status.HTTP_204_NO_CONTENT)


class SongsAPIView(APIView):
    def get(self, request):
        songs = Songs.objects.all()
        serializer = SongsSerializer(songs, many=True)
        return Response(data=serializer.data)


class SongsAPIView(ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer

