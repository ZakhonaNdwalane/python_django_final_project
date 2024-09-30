from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


# Contact Form
class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Message')

# Custom User Registration Form
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    #Override the form field widgets to add custom CSS classes
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'input-field'})
        self.fields['email'].widget.attrs.update({'class': 'input-field'})
        self.fields['password1'].widget.attrs.update({'class': 'input-field'})
        self.fields['password2'].widget.attrs.update({'class': 'input-field'})


# Login Form
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'input-field'}),
        label='Username'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'input-field'}),
        label='Password'
    )


# Risk Calculator Form
class RiskCalculatorForm(forms.Form):
    crop_type = forms.CharField(label='Crop Type', required=True)
    farm_size = forms.FloatField(label='Farm Size (hectares)', required=True)
    expected_yield = forms.FloatField(label='Expected Yield (tons)', required=True)
    weather_risk = forms.ChoiceField(label='Weather Risk', choices=[
        ('high', 'High'),
        ('moderate', 'Moderate'),
        ('low', 'Low')
    ])
    financial_stability = forms.ChoiceField(label='Financial Stability', choices=[
        ('high-risk', 'High Risk'),
        ('uncertain', 'Uncertain'),
        ('stable', 'Stable')
    ])
    pest_prevalence = forms.ChoiceField(label='Pest Prevalence', choices=[
        ('high', 'High'),
        ('moderate', 'Moderate'),
        ('low', 'Low')
    ])
    historical_prices = forms.CharField(label='Historical Prices (comma-separated)', required=True)


