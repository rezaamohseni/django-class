from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class SpecialService(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Team(models.Model):
    image = models.ImageField(upload_to="services", default="default.jpg")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ManyToManyField(Skill)
    description = models.TextField()
    status = models.BooleanField(default=False)
    facebook = models.CharField(max_length=220, default="#")
    twitter = models.CharField(max_length=220, default="#")
    instagram = models.CharField(max_length=220, default="#")
    linkdin = models.CharField(max_length=220, default="#")

    def __str__(self):
        return self.user.email


class Category(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Option(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    image = models.ImageField(upload_to="services", default="image.jpg")
    name = models.CharField(max_length=300)
    content = models.TextField()
    title = models.CharField(max_length=300)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    generals = models.ManyToManyField(Option)
    status = models.BooleanField(default=True)
    price = models.IntegerField()
    counted_view = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # def truncate_char(self):
    #     return str(self.description)[:10]


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    message = models.TextField(max_length=100)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
