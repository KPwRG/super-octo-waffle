from django.db import models

class Manager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):          
            errors['email'] = "Invalid email address."
        if len(postData['firstName']) < 2:
            errors["firstName"] = "First Name should be at least 2 characters."
        if len(postData['lastName']) < 2:
            errors["lastName"] = "Last Name should be at least 2 characters."
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters."
        return errors

class Registration (models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirmPassword = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Manager()

    def __repr__(self):
        return f"<class objects: {self.firstName} {self.lastName}({self.id})>"

