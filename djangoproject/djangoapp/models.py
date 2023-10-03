from django.db import models



# Create your models here.
class Food(models.Model):
    code = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=50, null=True)
    imported_t = models.CharField(max_length=50, null=True)
    url = models.CharField(max_length=300, null=True)
    creator = models.CharField(max_length=100, null=True)
    created_t = models.BigIntegerField(null=True)
    last_modified_t = models.BigIntegerField( null=True)
    product_name = models.CharField(max_length=300, null=True)
    quantity = models.CharField(max_length=100, null=True)
    brands = models.CharField(max_length=500, null=True)
    categories = models.CharField(max_length=500, null=True)
    labels = models.CharField(max_length=500, null=True)
    cities = models.CharField(max_length=500, null=True)
    purchase_places = models.CharField(max_length=300, null=True)
    stores = models.CharField(max_length=300, null=True)
    ingredients_text = models.CharField(max_length=5000, null=True)
    traces = models.CharField(max_length=500, null=True)
    serving_size = models.CharField(max_length=100, null=True)
    serving_quantity = models.CharField(max_length=100, null=True)
    nutriscore_score = models.CharField(max_length=100, null=True)
    nutriscore_grade = models.CharField(max_length=100, null=True)
    main_category = models.CharField(max_length=500, null=True)
    image_url = models.CharField(max_length=500, null=True)

