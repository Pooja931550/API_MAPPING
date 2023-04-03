from django.db import models
from django.contrib.auth.models import User
# from datetime import datetime
# from . forms1 import User_Registration,Project_Detail

# Create your models here.
# One to one relestionship



# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100, null=False)

#     def __str__(self):
#         return str(self.name)



# class Task(models.Model):
#     id = models.AutoField(primary_key=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
#     task_name = models.CharField(max_length=60, default='na')
#     task_date = models.DateField(null=True)



# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=30,unique=True)
#     description = models.CharField(max_length=100,default='na')
#     price = models.FloatField(blank=True,null=True)

#     def __str__(self):
#         return str(self.name)

# class Post(models.Model):
#     id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
#     name = models.CharField(max_length=30)
#     description = models.CharField(max_length=100,default='na')
#     price = models.FloatField(blank=True,null=True)

#     def __str__(self):
#         return str(self.name)


# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=30,unique=True)

#     def __str__(self):
#         return str(self.name)

# class Project(models.Model):
#     id = models.AutoField(primary_key=True)
#     user = models.ManyToManyField(User,null=True)
#     name = models.CharField(max_length=30)
#     email = models.EmailField(max_length=200,null=False)


#     def __str__(self):
#         return str(self.name)



##### MANY TO MANY RELESTIONSHIP THOUGH BY FROM ########

# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=30,unique=True)
#     pho_no = models.BigIntegerField(max_length=10,null=True)
#     email = models.EmailField(max_length=200,null=True)
#     password = models.CharField(max_length=30,null=True)
#     confirmation_password = models.CharField(max_length=50,null=True)


#     def __str__(self):
#         return str(self.name)

# class Project(models.Model):
#     # id = models.AutoField(primary_key=True)
#     user = models.ManyToManyField(User,null=True)
#     name = models.CharField(max_length=30)
#     task_name = models.CharField(max_length=200, null=True)
#     task_date = models.DateField(null=True,default=datetime.now)
#     email = models.EmailField(max_length=200,null=True)

#     def __str__(self):
#         return str(self.name)


#########################################################




################ ONE TO MANY RELESTIONSHIP THOUGH BY FROM USING THE SESSION ###################




class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30,null=True)
    password = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=50, null=True)

    def __str__(self):
        return self.username



class Student(models.Model):
    student_name = models.CharField(max_length=30)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    fathers_name = models.CharField(max_length=40)
    mothers_name = models.CharField(max_length=30)
    age = models.IntegerField(max_length=20,null=True)
    gender = models.CharField(max_length=10,null=True)
    level = models.CharField(max_length=250,null=True)
    department = models.CharField(max_length=25,null=True)
    address = models.CharField(max_length=250,null=True)
    email = models.EmailField(max_length=200,null=True)
    pho_no = models.BigIntegerField(max_length=10,null=True)
    dob = models.DateField(blank=True, null=True)
    password = models.CharField(max_length=30,null=True)
    confirmation_password = models.CharField(max_length=50,null=True)


    def __str__(self):
        return self.user.username











# class Person(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=128)

#     def __str__(self):
#         return self.name

# class Group(models.Model):
#     name = models.CharField(max_length=128)
#     members = models.ManyToManyField(Person, through='Membership')

#     def __str__(self):
#         return self.name

# class Membership(models.Model):
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     date_joined = models.DateField()
#     invite_reason = models.CharField(max_length=64)


