from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from models.models import *
from .forms import ContactForm
def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect('admin/dashboard/')
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.info(request, "Account not found !!!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            user_obj = authenticate(username=username, password=password)
            if user_obj and user_obj.is_superuser:
                login(request, user_obj)
                return redirect('admin/dashboard/')
            messages.info(request,"Invalid password !!!")
            return redirect('/')
        return render(request, 'login.html')
    except Exception as e:
        print(e)


def admin_dashboard(request):
    contacts = Contact_Model.objects.all()[:10]
    uncalled_contacts = Contact_Model.objects.filter(called=Boglanilmadi)[:10]
    called_contacts = Contact_Model.objects.filter(called=Boglanildi)[:10]
    context = {
        'contacts': contacts,
        'uncalled_contacts': uncalled_contacts,
        'called_contacts': called_contacts,
    }
    return render(request, 'dashboard.html', context)


def contact(request):
    contacts = Contact_Model.objects.all()[:100]

    context = {
        "contacts": contacts
    }

    return render(request, 'contact.html', context)


def Uncalled(request):
    contacts = Contact_Model.objects.filter(called=Boglanilmadi)[:100]

    context = {
        "contacts": contacts
    }

    return render(request, 'uncalled.html', context)


def called(request):
    contacts = Contact_Model.objects.filter(called=Boglanildi)[:100]

    context = {
        "contacts": contacts
    }

    return render(request, 'called.html', context)


def single_contact(request, id):
    contact = get_object_or_404(Contact_Model, id=id)
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        return redirect('uncalled')
    print(form)
    context = {
        "form": form,
        "contact": contact,
        "Boglanildi": Boglanildi,
        "Boglanilmadi": Boglanilmadi
    }
    return render(request, 'single.html', context)