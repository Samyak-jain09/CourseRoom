
from django.db import models
# from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver

class User(AbstractUser):
    name= models.CharField(max_length=200, null=True)
    email= models.EmailField(unique=True,null=True)
    bio= models.TextField(null=True)

    avatar= models.ImageField(null = True, default="avatar.svg")

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= []


class Topic(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    topic=models.ForeignKey(Topic, on_delete=models.SET_NULL,null=True)
    name= models.CharField(max_length=200)
    description= models.TextField(null=True, blank= True)
    participants=models.ManyToManyField(User, related_name= 'participants',blank=True )
    updated = models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-updated', '-created']

    def __str__(self):
        return self.name


class Message(models.Model):
    user= models.ForeignKey(User, on_delete= models.CASCADE)
    room= models.ForeignKey(Room, on_delete=models.CASCADE)
    body= models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['updated', 'created']

    def __str__(self):
        return self.body[0:50]





###############################################################################################################################

# class ThreadModel(models.Model):
#     user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
#     receiver= models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')

# class MessageModel(models.Model):
#     thread= models.ForeignKey('ThreadModel', related_name='+',on_delete=models.CASCADE,blank=True, null=True)
#     sender_user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
#     receiver_user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
#     body= models.CharField(max_length=100)
#     date= models.DateTimeField(default=timezone.now)