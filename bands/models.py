from django.db import models


class Band(models.Model):
    '''Creates instance of a band'''
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    total_members = models.PositiveIntegerField()
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Album(models.Model):
    '''Creates instance of an album'''
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    release_date = models.DateField()

    def __str__(self):
        return self.title


class Song(models.Model):
    '''Creates instance of a song'''
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    duration = models.DurationField()

    def __str__(self):
        return self.title
