from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Book,category
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden



# Create your views here.

def home(request):

    categories=category.objects.all()
    books=Book.objects.all()
    return render(request,'index.html',{'categories': categories,'books':books})


def signup_user(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken. Please choose a different one.')
            return redirect('signup_user')  # Redirect back to the signup page

        # Create a new user with a hashed password
        user=User.objects.create_user(username=username, email=email, password=password)

        # Optionally, log the user in right after signup
        login(request, user)

        print(username, email, password)
        return redirect('home')
    else:
        return render(request, 'signup.html', {})
    
def login_user(request):
    

    if request.method == 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(user=user,request=request)
            return redirect("home")
        else:
            messages.error(request,"Wrong Credintials.Please Try Agian !!!")
    else:
        return render(request,'login.html',{})
    
def logout_user(request):
    logout(request=request)
    return render(request,'login.html',{})
def category_view(request, category_name):
    # Use get_object_or_404 to fetch the category based on the category_name
    category = get_object_or_404(category,name=category_name)
    books=Book.objects.filter(catagory=category)
    # You can now use 'category' safely in the context
    return render(request, 'category_detail.html', {'category': category,'books': books})

@login_required
def download_book(request,id):
    book = get_object_or_404(Book, id=id)
    if request.user.is_authenticated:
        # Serve the book PDF for download
        response = redirect(book.pdf.url)
        response['Content-Disposition'] = f'attachment; filename="{book.title}.pdf"'
        return response
    else:
        return HttpResponseForbidden("You need to login to download this book.")


def search(request):
    pass