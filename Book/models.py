from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    manager = models.ForeignKey(User, on_delete = models.CASCADE)
    name     = models.CharField(max_length = 100)
    author   = models.CharField(max_length = 100)
    category = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    date     = models.DateField(auto_now=True)
    image    = models.ImageField(upload_to = 'images/')
    info     = models.TextField()
    status   = models.CharField(max_length = 100, choices = (
        ('Available', 'Avialable'),
        ('Not Available', 'Not Avialable'),
    ))
    phone    = models.PositiveIntegerField()  

    slug = models.SlugField(max_length=100, null=True, blank = True)

    def __str__(self):
        return self.name
    
    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Book.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment on {}'.format(self.book.name)



