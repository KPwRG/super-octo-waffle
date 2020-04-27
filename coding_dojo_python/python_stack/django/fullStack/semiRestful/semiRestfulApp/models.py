from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['showTitle']) < 2:
            errors["showTitle"] = "Show title should be at least 2 characters"
        if len(postData['showNetwork']) < 3:
            errors["showNetwork"] = "Show network should be at least 3 characters"
        if len(postData['description']) < 10:
            errors["description"] = "Show description should be at least 10 characters"
        return errors


class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects =ShowManager()

    def __repr__(self):
        return f"<class objects: {self.title} ({self.id})>"



