
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import MovieSerializer, DirectorSerializer, ReviewSerializer, MovieReviewSerializer, \
                        DirectorValidateSerializer, MovieValidateSerializer, ReviewValidateSerializer
from .models import Movie, Director, Review


class MovieReviewListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieReviewSerializer
    pagination_class = PageNumberPagination


class DirectorListCreateAPIView(ListCreateAPIView):
    '''list of objects'''
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    '''creation of objects'''
    def post(self, request, *args, **kwargs):
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        return Response(data={'message': 'Data received',
                              'director': DirectorSerializer(director).data},
                        status=status.HTTP_201_CREATED)


class DirectorDetailAPIView(RetrieveUpdateDestroyAPIView):
    '''get of object'''
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'pk'

    '''update of object'''
    '''there is no reason to write delete method in here, cause this method already exists in class'''
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)



class MovieListAPIView(ListCreateAPIView):
    '''List of movies'''
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination

    '''Creation of movies'''
    def post(self, request, *args, **kwargs):
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        title = request.data.get('title')
        description = request.data.get('description')
        film_duration = request.data.get('film_duration')
        director_id = request.data.get('director_id')
        movie = Movie.objects.create(title=title, description=description, film_duration=film_duration,  director_id=director_id)
        # director = Director.objects.create(name=request.data.get('name'))
        return Response(data={'message': 'Data received',
                              'movie': MovieSerializer(movie).data},
                              status=status.HTTP_201_CREATED)


class MovieDetailAPIView(APIView):
    def get(self, request, id):
        movie = self.get_object(id)
        serializer = MovieSerializer(movie, many=False)
        return Response(data=serializer.data)

    def delete(self, request, id):
        movie = self.get_object(id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        movie = self.get_object(id)
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Check if any fields were provided in the request data
        if not any(request.data.values()):
            return Response(data={'detail': 'At least one field is required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Update the movie object with the provided data
        if request.data.get('title'):
            movie.title = request.data['title']
        if request.data.get('description'):
            movie.description = request.data['description']
        if request.data.get('film_duration'):
            movie.film_duration = request.data['film_duration']
        if request.data.get('director_id'):
            movie.director_id = request.data['director_id']
        movie.save()

        serializer = MovieSerializer(movie)
        return Response(data={'message': 'Data received',
                              'movie': serializer.data},
                        status=status.HTTP_200_OK)

    def get_object(self, id):
        movie = get_object_or_404(Movie, id=id)
        return movie


class ReviewListAPIView(ListCreateAPIView):
    '''List of reviews'''
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination

    '''Creation of reviews'''
    def post(self, request, *args, **kwargs):
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = request.data.get('text')
        stars = request.data.get('stars')
        review = Review.objects.create(text=text, stars=stars)
        return Response(data={'message': 'Data received',
                              'review': ReviewSerializer(review).data},
                            status=status.HTTP_201_CREATED)


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    '''getting of review'''
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    '''updating of object'''
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     serializer = ReviewValidateSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     review.text = request.data.get('text')
    #     review.stars = request.data.get('stars')
    #     review.movie = request.data.get('movie')
    #     review.save()
    #     return Response(data={'message': 'Data received',
    #                           'review': ReviewSerializer(review).data},
    #                     status=status.HTTP_200_OK)





# @api_view(['GET'])
# def movie_reviews_view(request):
#     movie = Movie.objects.all()
#     serializer = MovieReviewSerializer(movie, many=True)
#     return Response(data=serializer.data)


# @api_view(['GET', 'POST'])
# def director_list_api_view(request):
#     if request.method == 'GET':
#         '''list of directors'''
#         directors = Director.objects.all()
#         serializer = DirectorSerializer(directors, many=True)
#         return Response(data=serializer.data)
#
#     elif request.method == 'POST':
#         '''creation of directors'''
#         serializer = DirectorValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(data=serializer.errors,
#                             status=status.HTTP_406_NOT_ACCEPTABLE)
#         name = request.data.get('name')
#         director = Director.objects.create(name=name)
#         return Response(data={'message': 'Data received',
#                               'director': DirectorSerializer(director).data},
#                         status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def director_detail_api_view(request):
#     try:
#         director = Director.objects.get(id=id)
#     except Director.DoesNotExist:
#         return Response(data={'detail': 'Director_not_found!'},
#                         status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = DirectorSerializer(director, many=False)
#         return Response(data=serializer.data)
#     elif request.method == 'DELETE':
#         director.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         director.name = request.data.get('name')
#         director.save()
#         return Response(data={'message': 'Data received',
#                               'director': DirectorSerializer(director).data},
#                         status=status.HTTP_200_OK)

#
# @api_view(['GET', 'POST'])
# def movie_list_api_view(request):
#     print(request.user)
#     if request.method == 'GET':
#         '''List of movies'''
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(data=serializer.data)
#     elif request.method == 'POST':
#         '''Creation of movies'''
#         serializer = MovieValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(data=serializer.errors,
#                             status=status.HTTP_406_NOT_ACCEPTABLE)
#         title = request.data.get('title')
#         description = request.data.get('description')
#         duration = request.data.get('duration')
#         director_id = request.data.get('director_id')
#         movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
#         # director = Director.objects.create(name=request.data.get('name'))
#         return Response(data={'message': 'Data received',
#                               'movie': MovieSerializer(movie).data},
#                               status=status.HTTP_201_CREATED)

#
# @api_view(['GET', 'DELETE', 'PUT'])
# def movie_detail_api_view(request, id):
#     try:
#         movie = Movie.objects.get(id=id)
#     except Movie.DoesNotExist:
#         return Response(data={'detail': 'Movie_not_found!'},
#                         status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = MovieSerializer(movie, many=False)
#         return Response(data=serializer.data)
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         serializer = MovieValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         movie.title = request.data.get('title')
#         movie.description = request.data.get('description')
#         movie.duration = request.data.get('duration')
#         movie.director_id = request.data.get('director_id')
#         movie.save()
#         return Response(data={'message': 'Data received',
#                               'movie': MovieSerializer(movie).data},
#                         status=status.HTTP_200_OK)

#
# @api_view(['GET', 'POST'])
# def review_list_api_view(request):
#     if request.method == 'GET':
#         '''List of reviews'''
#         reviews = Review.objects.all()
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(data=serializer.data)
#     elif request.method == 'POST':
#         '''Creation of reviews'''
#         serializer = ReviewValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         text = request.data.get('text')
#         stars = request.data.get('stars')
#         review = Review.objects.create(text=text, stars=stars)
#         return Response(data={'message': 'Data received',
#                               'review': ReviewSerializer(review).data},
#                         status=status.HTTP_201_CREATED)

#
# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail_api_view(request, id):
#     try:
#         review = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response(data={'detail': 'Review_not_found!'},
#                         status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = ReviewSerializer(review, many=False)
#         return Response(data=serializer.data)
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'PUT':
#         serializer = ReviewValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         review.text = request.data.get('text')
#         review.stars = request.data.get('stars')
#         review.movie = request.data.get('movie')
#         review.save()
#         return Response(data={'message': 'Data received',
#                               'review': ReviewSerializer(review).data},
#                         status=status.HTTP_200_OK)

