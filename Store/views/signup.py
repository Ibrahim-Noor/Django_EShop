from django.views import View
from django.shortcuts import redirect, render
from Store.models.customer import Customer
from django.contrib.auth.hashers import make_password


class Signupform(View):
    def validateCustomer(self, customer):
        error = None
        if len(customer.full_name) < 4:
            error = "Name must be more than 4 characters"
        elif len(customer.phone) != 11:
            error = "Enter a valid contact number"
        elif len(customer.password) < 6:
            error = "Password must be atleast 6 characters long"
        elif customer.isExists():
            error = "An account already exists with the given email"

        return error

    def get(self, request):
        return render(request, 'signuppage.html')

    def post(self, request):
        full_name = request.POST.get("name")
        phone = request.POST.get("c_number")
        email = request.POST.get("email")
        password = request.POST.get("password")

        customer = Customer(full_name=full_name, phone=phone,
                            email=email, password=password)

        values = {
            'name': full_name,
            'phone': phone,
            'email': email,
            'password': password
        }

        error = self.validateCustomer(customer)

        if not error:
            customer.password = make_password(customer.password)
            customer.register_customer()
            return redirect('homepage')
        else:
            data = {
                'error': error,
                'values': values
            }
            return render(request, 'signuppage.html', data)
