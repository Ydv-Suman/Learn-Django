from django.shortcuts import render, redirect

# Create your views here.

def contact_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email-address")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        return redirect("confirmation")

    return render(request, "contact/contact.html")


def confirmation(request):
    return render(request, "contact/confirmation.html")