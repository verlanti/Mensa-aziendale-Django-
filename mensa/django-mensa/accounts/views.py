from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .form import RegisterForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
class SignUp(generic.CreateView):
    """View Sign up che gestisce la funzione di registrazione
    di un nuovo utente. """
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


    def post(self, request, *args, **kwargs):
        """Funzione post che raccoglie i dati inseriti dal nuovo user.
           In caso di successo:
                    --> porta l'user alla pagina di login
           In caso di fallimento:
                    --> genera un errore e fa riprovare l'inserimento """
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                group = Group.objects.get(name=user.group)
                user.groups.add(group)
                return redirect('login')
            else:
                form = RegisterForm()
        return render(request, 'accounts/signup.html', {'form': form})
