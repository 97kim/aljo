from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from aljoadmin.models import Aljoadmin
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from aljoadmin.forms import CommentForm
from django.http import HttpResponseRedirect
from django.db.models import Count
# Create your views here.

class AljoadminLV(ListView):
    model = Aljoadmin

class AljoadminLikeLV(ListView):
    model = Aljoadmin

    def get_queryset(self):
        return Aljoadmin.objects.annotate(like_count=Count('like_users')).order_by('-like_count', '-create_dt')

class AljoadminStarbucksLV(ListView):
    model = Aljoadmin

    def get_queryset(self):
        return Aljoadmin.objects.annotate(like_count=Count('like_users')).filter(brand="스타벅스").order_by('-like_count','-create_dt')

class AljoadminEdiyaLV(ListView):
    model = Aljoadmin

    def get_queryset(self):
        return Aljoadmin.objects.annotate(like_count=Count('like_users')).filter(brand="이디야").order_by('-like_count','-create_dt')

class AljoadminGongchaLV(ListView):
    model = Aljoadmin

    def get_queryset(self):
        return Aljoadmin.objects.annotate(like_count=Count('like_users')).filter(brand="공차").order_by('-like_count','-create_dt')

@method_decorator(login_required, name="post")
class AljoadminDV(DetailView):
    model = Aljoadmin

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
            comment = form.save(commit=False)
            comment.aljo = aljo
            comment.writer = self.request.user
            comment.save()
            return HttpResponseRedirect(reverse('aljoadmin:detail', args=[aljo.slug]))
        else:
            return render(request, self.template_name, {'form': form})

class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_aljoadmin_list.html'
    model = Aljoadmin

    def get_queryset(self):
        return Aljoadmin.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context

@login_required
def like(request, slug):
    aljoadmin = get_object_or_404(Aljoadmin, slug=slug)
    if request.user in aljoadmin.like_users.all():
        aljoadmin.like_users.remove(request.user)
    else:
        aljoadmin.like_users.add(request.user)
    return redirect('aljoadmin:detail', aljoadmin.slug)

#def search(request):
#    q = request.POST.get('q', "")

#    menus = Aljoadmin.objects.filter(Q(foodname__icontains=q) | Q(recipe__icontains=q) | Q(brand__icontains=q) | Q(tags__name__icontains=q)).distinct()

#    if q:
#        return render(request, 'aljoadmin/aljoadmin_search.html', {'menus': menus, 'q': q})

#    else:
#        return render(request, 'aljoadmin/aljoadmin_search.html')

