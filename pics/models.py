from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)

    @property
    def preview(self):
        first = self.images.last()
        return first.image.url

    def __str__(self):
        return self.name


class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Picture(models.Model):
    avatar_thumbnail = ProcessedImageField(upload_to='avatars',
                                           processors=[ResizeToFill(100, 50)],
                                           format='JPEG',
                                           options={'quality': 60})
    pub_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(tags)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category, related_name="images", null=False, on_delete=models.CASCADE)

    @classmethod
    def search_by_title(cls, search_term):
        images = cls.objects.filter(description__contains=search_term)

        return images

    @classmethod
    def get_image_by_id(cls, id):
        return cls.objects.get(pk=id)

    @property
    def allinfo(self):
        info = {
            'cat': self.category,
            'desc': self.description,
            'image': self.image.url,
            'id': self.id
        }
        return str(info)
