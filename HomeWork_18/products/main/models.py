from django.db import models


class Model1(models.Model):
    part_id = models.AutoField(primary_key=True)
    part = models.CharField(max_length=100)
    cat = models.IntegerField()

    def __str__(self):
        return self.part


class Model2(models.Model):
    cat_numb = models.IntegerField()
    cat_name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.cat_name
