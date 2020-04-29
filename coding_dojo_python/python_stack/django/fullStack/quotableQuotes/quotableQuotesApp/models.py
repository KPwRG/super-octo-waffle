from django.db import models
import re
import bcrypt


class UserManager(models.Manager):

    def regisValidator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['fname']) < 2:
            errors['firstName'] = "First Name must be at least 2 characters!"
        if len(postData['lname']) < 2:
            errors['lastname'] = "Last Name must be at least 2 characters!"
        if len(postData['email']) < 1:
            errors['email'] = "Email is required!"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['emailformat'] = "Email is in invalid format!"
        else:
            usersWithEmail = User.objects.filter(email=postData['email'])
            if len(usersWithEmail) > 0:
                errors['emailTaken'] = "Email is already taken, please try another email address."
        if len(postData['pw']) < 8:
            errors['password'] = "Password must be at least 8 characters!"
        if postData['pw'] != postData['cpw']:
            errors['confirm'] = "Password and confirm password must match!"
        return errors

    def loginValidator(self, postData):
        errors = {}
        if len(postData['email']) < 1:
            errors['email'] = "Email is required"
        emailsExist = User.objects.filter(email=postData['email'])
        if len(emailsExist) == 0:
            errors['emailNotFound'] = "This email was not found. Please register first."
        else:
            user = emailsExist[0]
            if not bcrypt.checkpw(postData['pw'].encode(), user.password.encode()):
                errors['pw'] = "Password does not match"
        return errors


class QuoteManager(models.Manager):
    def validateQuote(self, postData):
        errors = {}
        if len(postData['quoterName']) < 1:
            errors['quoterNameRequired'] = "Quote name is required"
        elif len(postData['quote']) < 4:
            errors['quoteShort'] = "Quote name needs to be at least 4 characters"
        return errors


class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Quote(models.Model):
    quoterName = models.CharField(max_length=255, null=True)
    quote = models.TextField(null=True)
    uploader = models.ForeignKey(User, related_name='quote_uploaded', on_delete=models.CASCADE)
    favoritor = models.ManyToManyField(User, related_name='fav_items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()
