from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from aljouser.models import Aljouser
from django.urls import reverse
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from mysite.views import OwnerOnlyMixin
from aljouser.forms import CommentForm
from django.http import HttpResponseRedirect
from django.db.models import Count
# Create your views here.

class AljouserLV(ListView):
    model = Aljouser

class AljouserLikeLV(ListView):
    model = Aljouser

    def get_queryset(self):
        return Aljouser.objects.annotate(like_count=Count('like_users')).order_by('-like_count', '-create_dt')


class AljouserMypostLV(LoginRequiredMixin, ListView):
    model = Aljouser

    def get_queryset(self):
        return Aljouser.objects.filter(owner=self.request.user).order_by('-create_dt')

class AljouserStarbucksLV(ListView):
    model = Aljouser

    def get_queryset(self):
        return Aljouser.objects.filter(brand="스타벅스").order_by('-create_dt')
    
class AljouserEdiyaLV(ListView):
    model = Aljouser

    def get_queryset(self):
        return Aljouser.objects.filter(brand="이디야").order_by('-create_dt')
    
class AljouserGongchaLV(ListView):
    model = Aljouser

    def get_queryset(self):
        return Aljouser.objects.filter(brand="공차").order_by('-create_dt')

@method_decorator(login_required, name="post")
class AljouserDV(DetailView):
    model = Aljouser

    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
    #    context['disqus_id'] = f"menu-{self.object.id}-{self.object.slug}"
    #    context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
    #    context['disqus_title'] = f"{self.object.slug}"
    #    return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm(auto_id=False)
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST, auto_id=False)
        if form.is_valid():
            aljo = self.get_object()
            commentuser = form.save(commit=False)
            commentuser.aljo = aljo
            commentuser.writer = self.request.user
            commentuser.save()
            return HttpResponseRedirect(reverse('aljouser:detail', args=[aljo.id]))
        else:
            return render(request, self.template_name, {'form': form})

class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_aljouser_list.html'
    model = Aljouser

    def get_queryset(self):
        return Aljouser.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context

@login_required
def like(request, pk):
    aljouser = get_object_or_404(Aljouser, pk=pk)
    if request.user in aljouser.like_users.all():
        aljouser.like_users.remove(request.user)
    else:
        aljouser.like_users.add(request.user)
    return redirect('aljouser:detail', aljouser.pk)

class AljoCreateView(LoginRequiredMixin, CreateView):
    model = Aljouser
    fields = ['foodname', 'recipe', 'brand', 'role', 'image', 'tags']

    success_url = reverse_lazy('aljouser:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class AljoUpdateView(OwnerOnlyMixin, UpdateView):
    model = Aljouser
    fields = ['foodname', 'recipe', 'brand', 'role', 'image', 'tags']
    success_url = reverse_lazy('aljouser:index')


class AljoDeleteView(OwnerOnlyMixin, DeleteView) :
    model = Aljouser
    success_url = reverse_lazy('aljouser:index')