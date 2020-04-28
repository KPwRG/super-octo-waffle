from django.db import models
import re, bcrypt


class UserManager(models.Manager):
    def regis_validator(self, postData):
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors = {}
        if len(postData['firstName']) < 2:
            errors["firstName"] = "First Name should be at least 2 characters."
        if len(postData['lastName']) < 2:
            errors["lastName"] = "Last Name should be at least 2 characters."
        if len(postData['email']) < 1:
            errors["email"] = "Password required."
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address."
        else:
            userWithEmail = User.objects.filter(email=postData['email'])
            if len(userWithEmail) > 0:
                errors['emailTaken'] = "Email address is already taken. Please use another email address."
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters."
        if postData['password'] != postData['confirmPW']:
            errors['confirmPW'] = "Confirmation Password and Password do not match."
        return errors

    def login_validator(self, postData):
        errors ={}
        if len(postData['email']) < 1:
            errors["email"] = "Password required."
        emailExist = User.objects.filter(email=postData['email'])
        if len(emailExist) == 0:
            errors['emailNotFound'] = "Email not found. Please register"
        else:
            user = emailExist[0]
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors['password'] = "Password does not match."
        return errors


class User (models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self):
        return f"<class objects: {self.firstName} {self.lastName}({self.id})>"
