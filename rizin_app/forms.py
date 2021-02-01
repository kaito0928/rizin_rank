from .models import BantamRank,BantamPlayer,FeatherRank,FeatherPlayer
from django import forms

class BantamrankCreateForm(forms.ModelForm):
        one = forms.ModelChoiceField(label='1位',queryset=BantamPlayer.objects.all(),widget=forms.Select,empty_label='1位を選択')
        two = forms.ModelChoiceField(label='2位',queryset=BantamPlayer.objects.all(),widget=forms.Select,empty_label='2位を選択')
        three = forms.ModelChoiceField(label='3位',queryset=BantamPlayer.objects.all(),widget=forms.Select,empty_label='3位を選択')
        four = forms.ModelChoiceField(label='4位',queryset=BantamPlayer.objects.all(),widget=forms.Select,empty_label='4位を選択')
        five = forms.ModelChoiceField(label='5位',queryset=BantamPlayer.objects.all(),widget=forms.Select,empty_label='5位を選択')
        six = forms.ModelChoiceField(label='6位',queryset=BantamPlayer.objects.all(),widget=forms.Select,empty_label='6位を選択')
        seven = forms.ModelChoiceField(label='7位',queryset=BantamPlayer.objects.all(),widget=forms.Select,empty_label='7位を選択')
        eight = forms.ModelChoiceField(label='8位',queryset=BantamPlayer.objects.all(),widget=forms.Select,empty_label='8位を選択')
        nine = forms.ModelChoiceField(label='9位',queryset=BantamPlayer.objects.all(),widget=forms.Select,empty_label='9位を選択')
        ten = forms.ModelChoiceField(label='10位',queryset=BantamPlayer.objects.all(),widget=forms.Select,empty_label='10位を選択')

        class Meta:
            model = BantamRank

            fields = ('user','one','two','three','four','five','six','seven','eight','nine','ten',)
            widget = {'user': forms.TextInput(),}

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields['user'].widget.attrs['class'] = 'form-control'
            self.fields['user'].widget.attrs['placeholder'] = '作成者'
            self.fields['user'].widget.attrs['maxlength'] = '20'


class FeatherrankCreateForm(forms.ModelForm):
    one = forms.ModelChoiceField(label='1位', queryset=FeatherPlayer.objects.all(), widget=forms.Select,
                                 empty_label='1位を選択')
    two = forms.ModelChoiceField(label='2位', queryset=FeatherPlayer.objects.all(), widget=forms.Select,
                                 empty_label='2位を選択')
    three = forms.ModelChoiceField(label='3位', queryset=FeatherPlayer.objects.all(), widget=forms.Select,
                                   empty_label='3位を選択')
    four = forms.ModelChoiceField(label='4位', queryset=FeatherPlayer.objects.all(), widget=forms.Select,
                                  empty_label='4位を選択')
    five = forms.ModelChoiceField(label='5位', queryset=FeatherPlayer.objects.all(), widget=forms.Select,
                                  empty_label='5位を選択')
    six = forms.ModelChoiceField(label='6位', queryset=FeatherPlayer.objects.all(), widget=forms.Select,
                                 empty_label='6位を選択')
    seven = forms.ModelChoiceField(label='7位', queryset=FeatherPlayer.objects.all(), widget=forms.Select,
                                   empty_label='7位を選択')
    eight = forms.ModelChoiceField(label='8位', queryset=FeatherPlayer.objects.all(), widget=forms.Select,
                                   empty_label='8位を選択')
    nine = forms.ModelChoiceField(label='9位', queryset=FeatherPlayer.objects.all(), widget=forms.Select,
                                  empty_label='9位を選択')
    ten = forms.ModelChoiceField(label='10位', queryset=FeatherPlayer.objects.all(), widget=forms.Select,
                                 empty_label='10位を選択')

    class Meta:
        model = FeatherRank

        fields = ('user', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',)
        widget = {'user': forms.TextInput(), }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget.attrs['class'] = 'form-control'
        self.fields['user'].widget.attrs['placeholder'] = '作成者'
        self.fields['user'].widget.attrs['maxlength'] = '20'