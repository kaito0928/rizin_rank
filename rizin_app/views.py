from django.shortcuts import render
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from .models import BantamPlayer,FeatherPlayer,RightPlayer,BantamRank,FeatherRank,RightRank
from .forms import BantamrankCreateForm,FeatherrankCreateForm,RightrankCreateForm

class IndexView(generic.TemplateView):
    template_name = 'index.html'

def player_list(request):
    bantam_players = BantamPlayer.objects.all()
    feather_players = FeatherPlayer.objects.all()
    right_players = RightPlayer.objects.all()
    params = {
        'bantam_players': bantam_players,
        'feather_players': feather_players,
        'right_players': right_players,
    }
    return render(request,'player_list.html',params)


class BantamrankCreateView(generic.FormView):
    model = BantamRank
    template_name = 'bantamrank_create.html'
    form_class = BantamrankCreateForm
    success_url = reverse_lazy('rizin_app:bantamrank_list')

    def form_valid(self,form):
        bantamrank = form.save(commit=False)
        bantamrank.save()
        messages.success(self.request,'バンタム級ランキングを作成しました。')
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.success(self.request,'作成に失敗しました。')
        return super().form_invalid(form)


class FeatherrankCreateView(generic.FormView):
    model = FeatherRank
    template_name = 'featherrank_create.html'
    form_class = FeatherrankCreateForm
    success_url = reverse_lazy('rizin_app:featherrank_list')

    def form_valid(self,form):
        featherrank = form.save(commit=False)
        featherrank.save()
        messages.success(self.request,'フェザー級ランキングを作成しました。')
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.success(self.request,'作成に失敗しました。')
        return super().form_invalid(form)

class RightrankCreateView(generic.FormView):
    model = RightRank
    template_name = 'rightrank_create.html'
    form_class = RightrankCreateForm
    success_url = reverse_lazy('rizin_app:rightrank_list')

    def form_valid(self,form):
        rightrank = form.save(commit=False)
        rightrank.save()
        messages.success(self.request,'ライト級ランキングを作成しました。')
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.success(self.request,'作成に失敗しました。')
        return super().form_invalid(form)


class BantamrankListView(generic.ListView):
    model = BantamRank
    template_name = 'bantamrank_list.html'
    paginate_by = 2

    def get_queryset(self):
        bantamranks = BantamRank.objects.all().order_by('-created_at')
        return bantamranks

class FeatherrankListView(generic.ListView):
    model = FeatherRank
    template_name = 'featherrank_list.html'
    paginate_by = 3

    def get_queryset(self):
        featherranks = FeatherRank.objects.all().order_by('-created_at')
        return featherranks

class RightrankListView(generic.ListView):
    model = RightRank
    template_name = 'rightrank_list.html'
    paginate_by = 2

    def get_queryset(self):
        rightranks = RightRank.objects.all().order_by('-created_at')
        return rightranks
