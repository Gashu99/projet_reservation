from django import forms


class formreservation_chambres(forms.Form):
    username=forms.CharField(label="nom ",required=True,widget=forms.TextInput(attrs={'class': 'username'}))
    prenom=forms.CharField(label="prenom",required=True,widget=forms.TextInput(attrs={'class': 'prenom'}))
    password=forms.CharField(label='mot de passe ',widget=forms.PasswordInput(attrs={'class': 'mdp'}))
    confirmpassword=forms.CharField(label='confirmer mot de passe  ',widget=forms.PasswordInput(attrs={'class': 'mdp'}))
    Tel=forms.IntegerField(label='num_telephone',required=True,widget=forms.NumberInput(attrs={'class': 'tel'}))
    mail=forms.EmailField(label='Email',required=True,widget=forms.EmailInput(attrs={'class': 'mail'}))
    date_res=forms.DateField(label='date_reservation',required=True,widget=forms.DateTimeInput(attrs={'class': 'dr'}))