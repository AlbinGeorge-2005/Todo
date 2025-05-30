from django.db import models
from django.contrib.auth.models import User
# Create your models here.





class Todo(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    options  = {
    'pending' : 'pending',
    'completed' : 'completed',
    'ongoing' : 'ongoing'
    }
    status = models.CharField(max_length=50,choices=options)
    created_date = models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
# on_delete=models.CASCADE --> when we delete the user the user's created Todo's will get deleted
# ForeingnKey --> one person doing many jobs(so here, one user create many Todo's)
# makemigrations --> python file converted into query file because database only interact with queries
# migrate --> creating the model into database after makemigrations



