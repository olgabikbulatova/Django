from django import forms


class GameForm(forms.Form):
    gamename = forms.ChoiceField(choices=[('headtails', 'Орел и Решка'), ('cubes','Cubes'), ('hundred', 'Hundred')])
    roll = forms.IntegerField(min_value=1, max_value=64)
