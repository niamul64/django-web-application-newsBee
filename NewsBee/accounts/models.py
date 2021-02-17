from django.db import models
from django.contrib.auth.models import User # default user model import
# Create your models here.
from django.utils import timezone
class ExtentionUser(models.Model):  # extra fields for user
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    fullName= models.CharField(max_length=120, default="" , null=False , blank= False )
    country= models.CharField(max_length=120,default= "", null=False, choices=(
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


class Share(models.Model):                      # for saving the shared news in database
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    newsAuthor=models.CharField(max_length=120, default="" , null=True, blank= True )
    comment= models.CharField(max_length=120, default="" , null=True, blank= True )
    country= models.CharField(max_length=70, default= "", null=True)
    url = models.CharField(max_length=120, default="", null=True, blank=True)
    img =models.CharField(max_length=120, default="" , null=True, blank= True )
    newsDate = models.CharField(max_length=120, default="" , null=True, blank= True )
    category = models.CharField(max_length=120, default="", null=True, blank=True)
    description = models.CharField(max_length=120, default="", null=True, blank=True)
    title = models.CharField(max_length=120, default="", null=True, blank=True)
    share_date = models.DateTimeField(auto_now_add=True)