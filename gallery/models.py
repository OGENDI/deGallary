#
from django.db import models


# Create your models here.
class Location(models.Model):
    name_of_location = models.CharField(max_length=75)

    def __str__(self):
        return self.name_of_location

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Category(models.Model):
    name_of_category = models.CharField(max_length=75)

    def __str__(self):
        return self.name_of_category

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Image(models.Model):
    image = models.ImageField(upload_to='photos/')
    name_of_image = models.CharField(max_length=100)
    image_description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_of_image

    class Meta:
        ordering=['date_posted']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete

    @classmethod
    def update_image(cls,img_id,item):
        cls.objects.filter(id=img_id).update(image=item)

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id=id).all()
        return image

    @classmethod
    def get_images(cls):
        image = cls.objects.all()
        return image
    
    @classmethod
    def search_image_by_cat(cls,name_of_category):
        res_images = cls.objects.filter(category=Category.objects.filter(name_of_category__icontains=name_of_category).first()).all()
        return res_images

    @classmethod
    def filter_by_location(cls,locate):
        res_images = cls.objects.filter(location_icontains=locate)
        return res_images

        