from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ExtentionUser(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    fullName= models.CharField(max_length=120, default="" , null=False , blank= False )
    country= models.CharField(max_length=70,default= "", null=False, choices=(
        ('', 'Select'),
        ('Argentina','Argentina'),
        ('Australia','Australia'),
        ('Austria','Austria'),
        ('Belgium','Belgium'),
        ('Brazil', 'Brazil'),
        ('Bulgaria', 'Bulgaria'),
        ('Canada', 'Canada'),
        ('China', 'China'),
        ('Colombia', 'Colombia'),
        ('Czech Republic', 'Czech Republic'),
        ('Egypt', 'Egypt'),
        ('France', 'France'),
        ('Germany', 'Germany'),

        ('Greece', 'Greece'),
        ('Hong Kong', 'Hong Kong'),
        ('Hungary', 'Hungary'),
        ('India', 'India'),
        ('Indonesia', 'Indonesia'),
        ('Ireland', 'Ireland'),
        ('Israel', 'Israel'),
        ('Italy', 'Italy'),
        ('Japan', 'Japan'),
        ('Latvia', 'Latvia'),
        ('Lithuania', 'Lithuania'),
        ('Malaysia', 'Malaysia'),
        ('Mexico', 'Mexico'),
        ('Morocco', 'Morocco'),
        ('Netherlands', 'Netherlands'),
        ('New Zealand', 'New Zealand'),
        ('Nigeria', 'Nigeria'),
        ('Norway', 'Norway'),
        ('Philippines', 'Philippines'),

        ('Poland', 'Poland'),
        ('Portugal', 'Portugal'),
        ('Romania', 'Hungary'),
        ('Saudi Arabia', 'Saudi Arabia'),
        ('Serbia', 'Serbia'),
        ('Singapore', 'Singapore'),
        ('Slovakia', 'Slovakia'),
        ('Slovenia', 'Slovenia'),
        ('South Africa', 'South Africa'),
        ('South Korea', 'South Korea'),
        ('Sweden', 'Sweden'),
        ('Switzerland', 'Switzerland'),
        ('Taiwan', 'Taiwan'),
        ('Thailand', 'Thailand'),
        ('Turkey', 'Turkey'),

        ('UAE', 'UAE'),
        ('Ukraine', 'Ukraine'),
        ('United Kingdom', 'United Kingdom'),
        ('United States', 'United States'),
        ('Venuzuela', 'Venuzuela'),

    ))