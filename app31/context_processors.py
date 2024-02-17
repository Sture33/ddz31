from django.contrib.auth.models import User


def groups(request):
    user = User.objects.get(username=request.user.username)
    context = {'groups': user.groups.all()}
    return context