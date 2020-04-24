from django.db import models
    
class Guitars(models.Model):
    brand = models.CharField(max_length=45)
    model = models.TextField()
    production_year = models.DateTimeField()
    number_of_strings = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __repr__(self):
        return f"<Guitar objects: {self.brand} ({self.id})>"
