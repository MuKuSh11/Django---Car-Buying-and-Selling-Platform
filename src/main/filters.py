import django_filters

from .models import Listing

class ListingFilter(django_filters.FilterSet):
    class Meta:
        model = Listing
        fields = {'brand': {'exact'}, 'model': {'icontains'}, 'transmission': {'exact'}, 'mileage': {'lt', 'gt'}}