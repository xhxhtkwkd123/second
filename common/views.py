from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth import login, logout, authenticate


from common.forms import SignupForm

# Create your views here.



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            row_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=row_password)
            login(request, user)
            return redirect('blog:index')
        
    else:
        form = SignupForm()

    return render(request, 'common/signup.html', {'form':form})
