from django.db import models

# Create your models here.
class Knowledge(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    category = models.CharField(max_length=20)
    sub_category = models.CharField(max_length=40)
    search_word = models.CharField(max_length=200)
    article = models.TextField()
 
    class Meta:
        db_table = 'Knowledge';
