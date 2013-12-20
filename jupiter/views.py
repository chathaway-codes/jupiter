from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import messages

from jupiter.models import Reading, User, PhysicalActivity, Activity
from jupiter.forms import ReadingForm, UserForm, PhysicalActivityForm
from jupiter.forms import ActivityForm

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
    messages.success(self.request, "Saved the data!")
    return super(ReadingCreate, self).form_valid(form)

class UserDetail(DetailView):
  model = User

  def dispatch(self, request, *args, **kwargs):
    self.kwargs = kwargs
    self.request = request
    return super(UserDetail, self).dispatch(request, *args, **kwargs)

  def get_context_data(self, **kwargs):
    context = super(UserDetail, self).get_context_data(**kwargs)
    context['form'] = ReadingForm()
    context['physical_form'] = PhysicalActivityForm()
    return context

  def get_object(self):
    return self.request.user

class UserVisualize(DetailView):
  model = User
  template_name = 'jupiter/user_visualize.html'

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

class PhysicalActivityCreate(CreateView):
  model = PhysicalActivity
  form_class = PhysicalActivityForm

  def get_sucess_url(self):
    return reverse('home')

  def dispatch(self, request, *args, **kwargs):
    self.kwargs = kwargs
    self.request = request
    return super(PhysicalActivityCreate, self).dispatch(request, *args, **kwargs)

  def form_valid(self, form):
    form.instance.user = self.request.user
    messages.success(self.request, "Saved the data!")
    return super(PhysicalActivityCreate, self).form_valid(form)

class ActivityCreate(CreateView):
  model = Activity
  form_class = ActivityForm

  def get_sucess_url(self):
    return reverse('home')

  def form_valid(self, form):
    messages.success(self.request, "Activity added!")
    return super(ActivityCreate, self).form_valid(form)
