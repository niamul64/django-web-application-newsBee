from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ExtentionUser(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    fullName= models.CharField(max_length=120, default="" , null=False , blank= False )
    country= models.CharField(max_length=70,default= "", null=False, choices=(
        ('', 'Select'),
        ('ar','Argentina'),
        ('au','Australia'),
        ('at','Austria'),
        ('be','Belgium'),
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

    ))