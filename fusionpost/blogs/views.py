from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/register_done.html')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')