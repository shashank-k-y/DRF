from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from watchlist.models import WatchList, StreamingPlatform
from watchlist.api.serializers import (
    WatchListSerializer,
    StreamingPlatformSerializer
)


class WatchListView(APIView):

    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class WatchListDetailView(APIView):

    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(
                {"error": "Movie does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(
                {"error": "Movie does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(
                {"error": "Movie does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )

        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamingPlatFormView(APIView):

    def get(self, request):
        movies = StreamingPlatform.objects.all()
        serializer = StreamingPlatformSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamingPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class StreamingPlatformDetailView(APIView):

    def get(self, request, pk):
        try:
            platform = StreamingPlatform.objects.get(pk=pk)
        except StreamingPlatform.DoesNotExist:
            return Response(
                {"error": "Platform does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )

        serialzer = StreamingPlatformSerializer(platform)
        return Response(serialzer.data)

    def put(self, request, pk):
        try:
            platform = StreamingPlatform.objects.get(pk=pk)
        except StreamingPlatform.DoesNotExist:
            return Response(
                {"error": "Platform does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = StreamingPlatformSerializer(platform, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
