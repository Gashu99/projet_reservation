from django import forms


class formreservation_chambres(forms.Form):
    numero_chambre=forms.IntegerField(label='numero_chambre',required=True,widget=forms.NumberInput(attrs={'class': 'id_ch'}))
    username=forms.CharField(label="nom ",required=True,widget=forms.TextInput(attrs={'class': 'username'}))
    prenom=forms.CharField(label="prenom",required=True,widget=forms.TextInput(attrs={'class': 'prenom'}))
    Tel=forms.IntegerField(label='num_telephone',required=True,widget=forms.NumberInput(attrs={'class': 'tel'}))
    mail=forms.EmailField(label='Email',required=True,widget=forms.EmailInput(attrs={'class': 'mail'}))
    date_res=forms.DateField(label='date_reservation',required=True,widget=forms.DateTimeInput(attrs={'class': 'dr'}))