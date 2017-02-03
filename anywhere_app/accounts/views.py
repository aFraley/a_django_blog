from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View


def logout_view(request):
    logout(request)
    return redirect('accounts:login')


class Registration(View):
    form_class = UserCreationForm
    template_name = 'accounts/registration.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {
            'form': form
        })

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return redirect('blog:topics')
        return render(request, self.template_name, {
            'form': form
        })

