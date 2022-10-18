from django.db import models
from django.urls import reverse

class Eatery(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Create your models here.
class Review(models.Model):
    eatery = models.ForeignKey(
        Eatery, 
        on_delete=models.CASCADE
        )
    author = models.ForeignKey(
        'auth.User', 
        on_delete=models.CASCADE,
        related_name='reviews',
        null=True,
        )
    title = models.CharField(max_length=100)
    review = models.CharField(max_length=500)
    rating = models.IntegerField(default = 0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('r_r_detail', kwargs={'pk': self.pk})
