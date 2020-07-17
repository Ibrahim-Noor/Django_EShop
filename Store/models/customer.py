from django.db import models


class Customer(models.Model):
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name

    def register_customer(self):
        self.save()

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False

    @staticmethod
    def loginValidate(email):
        customer = Customer.objects.filter(email=email)
        if len(customer) > 0:
            return customer[0]
        return None
