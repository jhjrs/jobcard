from django import forms
from .models import JobCard
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

"""class JobCardForm(forms.ModelForm):
    class Meta:
        model = JobCard
        fields = ['details', 'photo']

    def clean_details(self):
        details = self.cleaned_data.get('details')
        if 'badword' in details:
            raise forms.ValidationError('Bad words are not allowed.')
        return details
        """

class JobCardForm(forms.ModelForm):
    CHOICES1 = [
        ('option1', 'YES'),
        ('option2', 'NO'),
        ('option3', 'Option 3'),
    ]

    CHOICES2 = [
        ('option1', 'YES'),
        ('option2', 'NO'),
        ('option3', 'Option 3'),
    ]

    Picture_of_Roof = forms.ChoiceField(choices=CHOICES1)
    Picture_of_Main = forms.ChoiceField(choices=CHOICES2)
    picture_of_roof = forms.ImageField()  # if this is supposed to be an image field
    picture_of_main = forms.ImageField()

    class Meta:
        model = JobCard
        fields = ['details',
                'photo',
                'Picture_of_Roof',
                'picture_of_roof',
                'Picture_of_Main',
                'picture_of_main',]
        
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user