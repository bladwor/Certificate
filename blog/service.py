from django.shortcuts import render

def error_404(request):
    template = 'blog/404_not_found.html'
    return render(request, template)
