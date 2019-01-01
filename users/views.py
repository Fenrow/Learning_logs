from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """Rejestracja nowego użytkownika"""

    if request.method != 'POST':
        #Wyświetlanie pustego formularza
        form = UserCreationForm()

    else:
        #Przetworzenie wypełnionego formularza
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #Zalogowanie użytkownika a następnie przekierowanie go na stronę główną
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    content = {'form': form}
    return render(request, 'users/register.html', content)
