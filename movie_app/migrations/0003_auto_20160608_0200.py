# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-08 02:00
from __future__ import unicode_literals

from django.db import migrations

import csv

def movie_data(apps, schema_editor):
    Movie = apps.get_model("movie_app", "Movie")
    with open("u.item", encoding="latin1") as outfile:
        movie = csv.DictReader(outfile, fieldnames=["movie_id", "movie_title", "release_date",
                                                    "video_release_date", "imdb_url", "unknown",
                                                    "action", "adventure", "animation", "children",
                                                    "comedy", "crime", "documentary", "drama", "fantasy",
                                                    "film_noir", "horror", "musical", "mystery", "romance",
                                                    "scifi", "thriller", "war", "western"], delimiter="|")

        for row in movie:
            Movie.objects.create(movie_id=int(row["movie_id"]), movie_title=row["movie_title"],
                                 release_date=row["release_date"], video_release_date=row["video_release_date"],
                                 imdb_url=row["imdb_url"], unknown=int(row["unknown"]), action=int(row["action"]),
                                 adventure=int(row["adventure"]), animation=int(row["animation"]),
                                 children=int(row["children"]), comedy=int(row["comedy"]), crime=int(row["crime"]),
                                 documentary=int(row["documentary"]), drama=int(row["drama"]),
                                 fantasy=int(row["fantasy"]), film_noir=int(row["film_noir"]),
                                 horror=int(row["horror"]), musical=int(row["musical"]),
                                 mystery=int(row["mystery"]), romance=int(row["romance"]), scifi=int(row["scifi"]),
                                 thriller=int(row["thriller"]), war=int(row["war"]), western=int(row["western"]))

    # raise Exception('yay2')


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_auto_20160607_1905'),
    ]

    operations = [
        migrations.RunPython(movie_data)

    ]
