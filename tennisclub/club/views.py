from django.shortcuts import render

# Main view
def main(request):
    return render(request, 'main.html')

# Members view
def members(request):
    return render(request, 'members.html')

# Courts view
def courts(request):
    return render(request, 'courts.html')

# About view
def about(request):
    return render(request, 'about.html')

# Contact view
def contact(request):
    return render(request, 'contact.html')