from django.views.generic import ListView, DetailView
from .models import User

class UserList(ListView):
    model = User
class UserDetail(DetailView):
    context_object_name = 'auser' # another user not request.user
    queryset = User.objects.all()


