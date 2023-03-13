from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, TemplateView
from django.views.generic.base import ContextMixin
from django.urls import reverse, reverse_lazy
from .management.commands.short_url import Command
from .forms import MakeForm
from .models import Link
from django.db.models import F


class MakeShortMixin(ContextMixin):
    def post(self, request, *args, **kwargs):
        make = request.POST['name']
        com = Command(make)
        com.handle()
        return HttpResponseRedirect(reverse('shorturl:result'))

    def get(self, request, *args, **kwargs):
        form = MakeForm()
        return render(request, 'shorturl/make.html', context={'form': form})


class ShortView(MakeShortMixin, CreateView):
    template_name = 'shorturl/make.html'


class ResultView(ListView):
    model = Link
    template_name = 'shorturl/result.html'
    paginate_by = 5

    # Link.objects.all().update(count=F("count") + 1)

    def get_queryset(self):
        return Link.objects.select_related().all()
