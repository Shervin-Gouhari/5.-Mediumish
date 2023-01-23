from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from datetime import datetime
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="published")


class Article(models.Model):
    class Meta():
        ordering = ("-created",)
        
    def __str__(self) -> str:
        return f"{self.title} written by: {self.author}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            now = datetime.now()
            self.slug = f"{slugify(self.title)}-{str(now.year)}-{str(now.month)}-{str(now.day)}-{str(now.hour)}-{str(now.minute)}-{str(now.second)}"
            self.save()
            
    def get_absolute_url(self):
        return reverse("articles:detail", kwargs={"slug": self.slug})
    
    STATUS_OF_ARTICLES = (
        ("checking", "Checking"),
        ("rejected", "Rejected"),
        ("published", "Published")
    )
    
    title = models.CharField(max_length=300)
    content = models.TextField()
    # created = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    status = models.CharField(max_length=50, choices=STATUS_OF_ARTICLES, default="checking")
    objects = models.Manager()
    published = PublishedManager()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="articles/%Y/%m/%d")
    