from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name
    

class SearcherLocation(models.Model):
    searcher = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.searcher.username} - {self.location.name}"

class LostItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=255)
    description = models.TextField()
    # image = models.ImageField(upload_to="lost_items/", blank=True, null=True)

    def __str__(self):
        return self.heading
    
    

class ItemLocation(models.Model):
    itemLoactionId = models.AutoField(primary_key=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    lost_item = models.ForeignKey(LostItem, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.lost_item.heading} - {self.location.name}"

    class Meta:
        permissions = [
            ("can-create-permissions", "Allows user to create permissions")
        ]
