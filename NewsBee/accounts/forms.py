from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ExtentionUser


class UserReg(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2' )


class ExtentUser(forms.ModelForm):
    fullName = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    select = (
        ('', 'Select'),
        ('ar', 'Argentina'),
        ('au', 'Australia'),
        ('at', 'Austria'),
        ('be', 'Belgium'),
        ('br', 'Brazil'),
        ('bg', 'Bulgaria'),
        ('ca', 'Canada'),
        ('cn', 'China'),
        ('co', 'Colombia'),
        ('cz', 'Czech Republic'),
        ('eg', 'Egypt'),
        ('fr', 'France'),
        ('de', 'Germany'),

        ('gr', 'Greece'),
        ('hk', 'Hong Kong'),
        ('hu', 'Hungary'),
        ('in', 'India'),
        ('id', 'Indonesia'),
        ('Ie', 'Ireland'),
        ('il', 'Israel'),
        ('it', 'Italy'),
        ('jp', 'Japan'),
        ('lv', 'Latvia'),
        ('lt', 'Lithuania'),
        ('my', 'Malaysia'),
        ('mx', 'Mexico'),
        ('ma', 'Morocco'),
        ('nl', 'Netherlands'),
        ('nz', 'New Zealand'),
        ('ng', 'Nigeria'),
        ('no', 'Norway'),
        ('ph', 'Philippines'),

        ('pl', 'Poland'),
        ('pt', 'Portugal'),
        ('ro', 'Hungary'),
        ('sa', 'Saudi Arabia'),
        ('rs', 'Serbia'),
        ('sg', 'Singapore'),
        ('sk', 'Slovakia'),
        ('si', 'Slovenia'),
        ('za', 'South Africa'),
        ('kr', 'South Korea'),
        ('se', 'Sweden'),
        ('ch', 'Switzerland'),
        ('tw', 'Taiwan'),
        ('th', 'Thailand'),
        ('tr', 'Turkey'),

        ('ae', 'UAE'),
        ('ua', 'Ukraine'),
        ('gb', 'United Kingdom'),
        ('us', 'United States'),
        ('ve', 'Venuzuela'),

    )

    class Meta:
        model = ExtentionUser
        fields = ('fullName', 'country')