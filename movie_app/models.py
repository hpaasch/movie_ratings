from django.db import models

# Create your models here.


class Movies(models.Model):
    movie_id = models.IntegerField()
    movie_title = models.CharField(max_length=75)
    release_date = models.CharField(max_length=15)
    video_release_date = models.CharField(max_length=15, default="")
    imdb_url = models.CharField(max_length=300)
    unknown = models.IntegerField()
    action = models.IntegerField()
    adventure = models.IntegerField()
    animation = models.IntegerField()
    children = models.IntegerField()
    comedy = models.IntegerField()
    crime = models.IntegerField()
    documentary = models.IntegerField()
    drama = models.IntegerField()
    fantasy = models.IntegerField()
    film_noir = models.IntegerField()
    horror = models.IntegerField()
    musical = models.IntegerField()
    mystery = models.IntegerField()
    romance = models.IntegerField()
    scifi = models.IntegerField()
    thriller = models.IntegerField()
    war = models.IntegerField()
    western = models.IntegerField()

    def __str__(self):
        return self.movie_title


class Reviewers(models.Model):
    user_id = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10, null=True)
    occupation = models.CharField(max_length=15)

    def __str__(self):
        return self.occupation


class Ratings(models.Model):
    user_id = models.ForeignKey(Reviewers)
    item_id = models.ForeignKey(Movies)
    rating = models.IntegerField()
    timestamp = models.IntegerField()

    def __str__(self):
        return self.rating
