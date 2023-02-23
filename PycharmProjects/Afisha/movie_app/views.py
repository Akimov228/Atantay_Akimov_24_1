from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MovieSerializer, DirectorSerializer, ReviewSerializer, MovieReviewSerializer
from .models import Movie, Director, Review


@api_view(['GET'])
def movie_reviews_view(request):
    movie = Movie.objects.all()
    serializer = MovieReviewSerializer(movie, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def director_list_api_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'detail': 'Director_not_found!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = DirectorSerializer(director, many=False)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_list_api_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'detail': 'movie_not_found!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializer(movie, many=False)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'detail': 'Review_not_found!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewSerializer(review, many=False)
    return Response(data=serializer.data)







# @api_view(['GET'])
# def test_api(request):
#     dict = {
#         'text': 'Hello World',
#         'int': 5,
#         'float': 2.5,
#         'list': ['Hello World'],
#         'set': {"Hello World", },
#     }
#     return Response(data=dict, status=200)