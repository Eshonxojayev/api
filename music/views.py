from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist, Albom, Songs
from .serializers import ArtistSerializer, AlbomSerializer, SongsSerializer
from rest_framework import status
from rest_framework.viewsets import ModelViewSet


class LandingPageAPIView(APIView):
    def get(self, request):
        return Response(data={"message": "Hi lazy developers"})

    def post(self, request):
        return Response(data={"post api": "This is post request api"})

class ArtistAPIView(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(data=serializer.data)

# class AlbomAPIView(APIView):
#     def get(self, request):
#         alboms = Albom.objects.all()
#         serializer = AlbomSerializer(alboms, many=True)
#         return Response(data=serializer.data)
class AlbomAPIViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer


class SongsAPIView(APIView):
    def get(self, request):
        songs = Songs.objects.all()
        serializer = SongsSerializer(songs, many=True)
        return Response(data=serializer.data)


class SongDetailAPIView(APIView):
    def get(self, request, id):
        try:
            song = Songs.objects.get(id=id)
            serializer = SongsSerializer(song)
            return Response(data=serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def patch(self, request, id):
        song = Songs.objects.get(id=id)
        serializer = SongsSerializer(instance=song, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, id):
        song = Songs.objects.get(id=id)
        serializer = SongsSerializer(instance=song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        song = Songs.objects.get(id=id)
        song.delete()
        return Response(data={}, status=status.HTTP_204_NO_CONTENT)


































    # def patch(self, request, id):
    #     song = Songs.objects.get(id=id)
    #     serializer = SongsSerializer(song)
    #     return Response(data=serializer.data)
    #
    # def delete(self, request, id):
    #     song = Songs.objects.get(id=id)
    #     serializer = SongsSerializer(song)
    #     return Response(data=serializer.data)
    #
    # def put(self, request, id):
    #     song = Songs.objects.get(id=id)
    #     serializer = SongsSerializer(song)
    #     return Response(data=serializer.data)
    #
