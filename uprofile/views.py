from django.views.generic import ListView, DetailView
from .models import User

class UserList(ListView):
    model = User
class UserDetail(DetailView):
    queryset = User.objects.all()


