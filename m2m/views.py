from m2m.models import Group
from django.http import HttpResponse


def create_group(request):
    g = Group.objects.create(name=request.POST["name"])
    return HttpResponse(g)
