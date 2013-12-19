from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from jupiter.models import Reading
from jupiter.forms import ReadingForm

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

