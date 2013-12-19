from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from jupiter.models import Reading, User
from jupiter.forms import ReadingForm, UserForm

class ReadingCreate(CreateView):
  model = Reading
  form_class = ReadingForm

  def get_sucess_url(self):
    return reverse('home')

  def dispatch(self, request, *args, **kwargs):
    self.kwargs = kwargs
    self.request = request
    return super(ReadingCreate, self).dispatch(request, *args, **kwargs)

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(ReadingCreate, self).form_valid(form)

class UserDetail(DetailView):
  model = User

  def dispatch(self, request, *args, **kwargs):
    self.kwargs = kwargs
    self.request = request
    return super(UserDetail, self).dispatch(request, *args, **kwargs)

  def get_object(self):
    return self.request.user

class UserEdit(UpdateView):
  model = User
  form_class = UserForm

  def get_sucess_url(self):
    return reverse('home')

  def dispatch(self, request, *args, **kwargs):
    self.kwargs = kwargs
    self.request = request
    return super(UserEdit, self).dispatch(request, *args, **kwargs)

  def get_object(self):
    return self.request.user
