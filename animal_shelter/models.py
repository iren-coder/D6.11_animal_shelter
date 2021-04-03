from django.db import models
from datetime import date


class Animal(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, null=True)
    eye_color = models.CharField(max_length=100, null=True)
    description = models.TextField()
    certificate = models.BooleanField(default=False)
    date_of_arrival = models.DateField(default=date.today)

    CAT = 'C'
    DOG = 'D'
    PARROT = 'P'
    KIND_OF_ANIMAL = [
        (CAT, 'Cat'),
        (DOG, 'Dog'),
        (PARROT, 'Parrot'),
    ]
    kind_of_animal = models.CharField(max_length=2, choices=KIND_OF_ANIMAL, default=CAT)

    MALE = 'M'
    FEMALE = 'F'
    SEX = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    sex = models.CharField(max_length=1, choices=SEX, null=True)

    image = models.ImageField(upload_to='static/images/animals_image/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    WORK_POSITION = [
        ('PRESIDENT', 'President'),
        ('VICE PRESIDENT', 'Vice president'),
        ('MANAGER', 'Manager'),
        ('TRAINEE', 'Trainee'),
    ]
    position = models.CharField(verbose_name='Position', max_length=50,
                                choices=WORK_POSITION, default='Trainee')
    image = models.ImageField(upload_to='static/images/animals_image/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.name

    @property
    def photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url


