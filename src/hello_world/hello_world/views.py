from django.http import HttpResponse


def hello_view(request):
    html_content = "<h1> Hello, world!</h1>"
    return HttpResponse(html_content)
