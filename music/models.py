from django.db import models
from django.core.urlresolvers import reverse


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('music:detail',kwargs={'pk':self.pk}) # Set 'pk' value to current albuminstance.

    def __str__(self):
        return self.artist + " - " + self.album_title



"""  Each song to be linked to an Album instance """
class Song(models.Model):
    """ If an album deleted then remove song instance of that album """
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    #song_id = models.IntegerField()
    is_favorite = models.BooleanField(default=False)


    def __str__(self):
        return self.song_title + " - " + self.file_type


