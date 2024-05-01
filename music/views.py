from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist, Albom, Songs
from .serializers import ArtistSerializer, AlbomSerializer, SongsSerializer
import json

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

class AlbomAPIView(APIView):
    def get(self, request):
        alboms = Albom.objects.all()
        serializer = AlbomSerializer(alboms, many=True)
        return Response(data=serializer.data)

class SongsAPIView(APIView):
    def get(self, request):
        songs = Songs.objects.all()
        serializer = SongsSerializer(songs, many=True)
        data = serializer.data
        # with open("../data.json", "w") as file:
        #     file_data = json.load(file)
        #     songs = file_data["songs"]
        # with open("../data.json", "w") as f:
        #     json.dump(data, f)
        # print("--------", data)
        return Response(data=serializer.data)