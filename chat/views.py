from django.shortcuts import render, redirect

def chatPage(request):
    if not request.user.is_authenticated:
        return redirect("login-user")
    return render(request, "chat/chatPage.html", {})
