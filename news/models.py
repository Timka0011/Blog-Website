from django.db import models
from accounts.models import CustomUser
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Region(models.Model):
    region = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.region


class News(models.Model):
    category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    images = models.ImageField(upload_to="image/", blank=True, null=True)
    timezone = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "New"
        verbose_name_plural = "News"


class Team(models.Model):
    name = models.CharField(max_length=150, unique=True)
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"


class Contact(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self) -> str:
        return self.fullname
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

