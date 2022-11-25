from django_filters import FilterSet
from .models import Advertise


class AdFilter(FilterSet):
   class Meta:
       model = Advertise
       fields = {
           'header': ['icontains'],
           'time_pub': ['gt'],
       }