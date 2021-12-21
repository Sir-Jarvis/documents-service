from django.db import models

# Create your models here.
class Document(models.Model):
    document = models.FileField(upload_to="myFiles")
    nom = models.CharField(max_length=50)
    typeFile = models.CharField(max_length=50)
    date_creation = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return str(self.date_creation) if self.date_creation else ''
    
