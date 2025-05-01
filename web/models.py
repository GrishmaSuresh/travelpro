from django.db import models


class destination(models.Model):
    title = models.CharField(max_length=100, default='none')
    msg = models.CharField(max_length=100, default='none')
    pic = models.ImageField(upload_to='media/pics')
    fee = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class post_blogs(models.Model):
    Name = models.CharField(max_length=20)
    Date = models.DateField()
    Title = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='media/pics', default='none')
    Description = models.TextField(max_length=300)

    def __str__(self):
        return self.Name
