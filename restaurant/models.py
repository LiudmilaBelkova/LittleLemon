from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return str(self.booking_date) + ' ' + self.name

# class Booking(models.Model):
#     first_name = models.CharField(max_length=200)
#     reservation_date = models.DateField()
#     reservation_slot = models.SmallIntegerField(default=10)

#     def __str__(self): 
#         return self.first_name + ": " + self.reservation_slot



class Menu(models.Model):
    title = models.CharField(max_length=255)
    menu_item_description = models.TextField(max_length=1000, default='') 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)} : {str(self.inventory)}'

