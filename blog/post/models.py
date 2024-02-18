from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True,
                                   blank=True)
    content = models.TextField()
    user = models.ForeignKey(to='user.User',
                             on_delete=models.CASCADE)
    category = models.ForeignKey(to=Category,
                                 on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/media/', null=True,blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


