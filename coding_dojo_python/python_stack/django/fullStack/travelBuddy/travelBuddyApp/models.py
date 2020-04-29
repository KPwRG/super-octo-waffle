from django.db import models
import re, bcrypt


class UserManager(models.Manager):
    def regis_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors["name"] = "Name should be at least 3 characters."
        if len(postData['userName']) < 3:
            errors["userName"] = "Username should be at least 3 characters."
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters."
        if postData['password'] != postData['confirmPW']:
            errors['confirmPW'] = "Confirmation Password and Password do not match."
        return errors

    def login_validator(self, postData):
        errors ={}
        if len(postData['userName']) < 1:
            errors['userName'] = 'Username is required'
        userExist = User.objects.filter(userName=postData['userName'])
        if len(userExist) == 0:
            errors['userNameNotFound'] = "This Username was not found. Please register."
        else:
            user = userExist[0]
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors['password'] = "Password does not match."
        return errors

class TripManager(models.Manager):
    def validateItem(self, postData):
        errors = {}
        if len(postData['dest']) < 1:
            errors['destRequired'] = "Destination is required."
        if len(postData['desc']) < 1:
            errors['descRequired'] = "Description is required."
        if len(postData['tdFrom']) < 1:
            errors['tdFromRequired'] = "Travel Date From is required."
        if len(postData['tdTo']) < 1:
            errors['tdToRequired'] = "Travel Date To is required."
        if postData['tdTo'] < postData['tdFrom']:
            errors['tdToBeforetdFrom'] = "Travel Date To can not be earlier than Travel Date From."
        return errors

class User (models.Model):
    name = models.CharField(max_length=255)
    userName = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self):
        return f"<class objects: {self.firstName} {self.lastName}({self.id})>"

class Trip (models.Model):
    dest = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    tdFrom = models.DateField()
    tdTo = models.DateField()
    travler = models.ManyToManyField(User, related_name = 'travel')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripManager()

    def __repr__(self):
        return f"<class objects: {self.dest}({self.id})>"