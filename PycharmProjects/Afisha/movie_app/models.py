from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def movies_count(self):
        count = self.movies_quantity.all().count()
        return count






class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    duration = models.FloatField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='movies_quantity')

    def __str__(self):
        return self.title

    def filtered_reviews(self):
        return self.movie_reviews.filter(stars__gt=3)


    def director_name(self):
        try:
            return self.director.name
        except:
            return ''

    @property
    def rating(self):
        count = self.movie_reviews.all().count()
        stars = sum([i.stars for i in self.movie_reviews.all()])
        return stars // count


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, related_name='movie_reviews')
    text = models.TextField(null=True, blank=True)
    stars = models.IntegerField(choices=([i, i * '*'] for i in range(1, 6)))
