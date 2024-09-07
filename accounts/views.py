from django.shortcuts import render
from .forms import RegistrationForm

def register(request):
    success_message = None
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # If the form is valid, display a success message
            success_message = "Registration successful! Your password is strong."
            form = RegistrationForm()  # Reset the form after successful submission
        else:
            print(form.errors)  # Print any validation errors
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form, 'success_message': success_message})
