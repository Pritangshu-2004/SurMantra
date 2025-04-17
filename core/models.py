from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('Bass', 'Bass'),
        ('Classical', 'Classical'),
        ('Instruments', 'Instruments'),
        ('Pop', 'Pop'),
        ('Jazz', 'Jazz'),
        ('Rock', 'Rock'),
        ('Western', 'Western'),
        ('Hip-Hop', 'Hip-Hop'),
        ('Electronic', 'Electronic'),
        ('Folk', 'Folk'),
        ('Blues', 'Blues'),
        ('Reggae', 'Reggae'),
        ('Country', 'Country'),
        ('Metal', 'Metal'),
        ('World', 'World'),
        # add more as needed
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES, default='Pop')
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)# add image field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title