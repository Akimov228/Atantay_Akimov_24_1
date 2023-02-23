from rest_framework import serializers
from .models import Director, Movie, Review



class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    stars = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "title reviews rating stars".split()


    def get_stars(self, movie):
        return [i.stars for i in movie.movie_reviews.all()]


    def get_reviews(self, movie):
        return [i.text for i in movie.movie_reviews.all()]


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name movies_count'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars '.split()


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    movie_reviews = ReviewSerializer(many=True)
    filtered_reviews = ReviewSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration',
                  'director', 'director_name', 'filtered_reviews', 'movie_reviews']


