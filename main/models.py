from django.db import models

EQUIPMENT_CHOICES = (
    ('full', 'Полная'),
    ('partial', 'Частичная')
)


class Car(models.Model):  # main_car
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    equipment = models.CharField(max_length=20, choices=EQUIPMENT_CHOICES)
    image = models.ImageField(upload_to='cars')

    class Meta:
        ordering = ['-year']
        db_table = 'car'
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return f'{self.model} {self.year} {self.color}'


class Sale(models.Model):
    client = models.CharField(max_length=100)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='sales')
    created_at = models.DateTimeField(auto_now_add=True)
