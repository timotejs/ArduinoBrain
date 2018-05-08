from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.TextField(default='')
    thumbnail = models.ImageField(upload_to='static/images')
    image = models.ImageField(upload_to='static/images')
    schematic = models.ImageField(upload_to='static/images')
    code = models.TextField(default='')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Part(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='static/images')
    name = models.CharField(max_length=50, default='')
    link = models.URLField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
