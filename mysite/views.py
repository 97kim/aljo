from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin
from aljoadmin.models import Aljoadmin
from aljouser.models import Aljouser
from django.db.models import Q
from django.shortcuts import render

class HomeView(ListView):
    context_object_name = 'home'
    template_name = 'home.html'
    queryset = Aljoadmin.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['aljoadmin_list'] = Aljoadmin.objects.all()
        context['aljouser_list'] = Aljouser.objects.all()
        #context['aljoadmin_list'] = Aljoadmin.objects.all()[:3]
        #context['aljouser_list'] = Aljouser.objects.all()[:3] #최근 글 3개 불러옴
        return context

class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/delete the object"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.owner:
            self.handle_no_permission()
        return super().get(request, *args, **kwargs)
    
def search(request):
    q = request.POST.get('q', "")

    menus = Aljoadmin.objects.filter(Q(foodname__icontains=q) | Q(recipe__icontains=q) | Q(brand__icontains=q) | Q(tags__name__icontains=q)).distinct()
    usermenus = Aljouser.objects.filter(Q(foodname__icontains=q) | Q(recipe__icontains=q) | Q(brand__icontains=q) | Q(tags__name__icontains=q)).distinct()

    if q:
        return render(request, 'search.html', {'menus': menus, 'q': q, 'usermenus': usermenus})

    else:
        return render(request, 'search.html')

def brand(request):

    starbucks = Aljoadmin.objects.filter(Q(brand='스타벅스')).distinct()
    starbucksuser = Aljouser.objects.filter(Q(brand='스타벅스')).distinct()

    return render(request, 'brand.html', {'starbucks': starbucks, 'starbucksuser': starbucksuser})

def brand2(request):

    ediya = Aljoadmin.objects.filter(Q(brand='이디야')).distinct()
    ediyauser = Aljouser.objects.filter(Q(brand='이디야')).distinct()

    return render(request, 'brand2.html', {'ediya':ediya, 'ediyauser':ediyauser})

def brand3(request):

    gongcha = Aljoadmin.objects.filter(Q(brand='공차')).distinct()
    gongchauser = Aljouser.objects.filter(Q(brand='공차')).distinct()

    return render(request, 'brand3.html', {'gongcha':gongcha, 'gongchauser':gongchauser})