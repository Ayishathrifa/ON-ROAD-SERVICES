from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    usertype = models.CharField(max_length=200)

class service(models.Model):
    service_name=models.CharField(max_length=200)

class worker(models.Model):
    worker_name=models.CharField(max_length=200)
    availability = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=200)
    LOGIN = models.ForeignKey(login,default=1,on_delete=models.CASCADE)


class user(models.Model):
    user_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=200)
    LOGIN = models.ForeignKey(login, default=1, on_delete=models.CASCADE)

class own_service(models.Model):
    WORKER=models.ForeignKey(worker,default=1,on_delete=models.CASCADE)
    SERVICE=models.ForeignKey(service,default=1,on_delete=models.CASCADE)
    Amount=models.IntegerField

class request_service(models.Model):
    time=models.CharField(max_length=200)
    Date=models.CharField(max_length=200)
    latitude=models.CharField(max_length=200)
    longitude = models.CharField(max_length=200,default=1)
    OWN_SERVICE=models.ForeignKey(own_service,default= 1,on_delete=models.CASCADE)
    USER=models.ForeignKey(user,default=1,on_delete=models.CASCADE)
    status=models.CharField(max_length=200)

class rating_reviews(models.Model):
    USER=models.ForeignKey(user,default=1,on_delete=models.CASCADE)
    Ratings=models.CharField(max_length=100)
    Reviews=models.CharField(max_length=100)
    WORKER=models.ForeignKey(worker,default=1,on_delete=models.CASCADE)

