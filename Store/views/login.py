from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from Store.models.customer import Customer
from django.views import View
from django.core import serializers
from django.urls import reverse


class Loginform(View):
    return_url = None

    def get(self, request):
        Loginform.return_url = request.GET.get('returnURL')
        print("return url", self.return_url)
        return render(request, 'loginpage.html')

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        customer = Customer.loginValidate(email)
        if customer:
            if check_password(password, customer.password):
                customer_data = serializers.serialize('json', [customer, ])
                request.session['customer'] = customer_data
                if self.return_url:
                    return_url_temp = self.return_url
                    Loginform.return_url = ""
                    return HttpResponseRedirect(return_url_temp)
                else:
                    return redirect(reverse("homepageloggedin", kwargs={'name': customer.full_name}))

            else:
                data = {
                    'error': "Invalid email or password",
                    'email': email
                }
            return render(request, 'loginpage.html', data)
        else:
            data = {
                'error': "Invalid email or password",
                'email': email
            }
            return render(request, 'loginpage.html', data)


def logout(request):
    request.session.clear()
    return redirect('login')
