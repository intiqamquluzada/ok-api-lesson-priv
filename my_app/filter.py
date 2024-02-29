from my_app.models import Model,Product

import django_filters


class ModelFilter(django_filters.FilterSet):
    class Meta:
        model = Model
        fields = ('marka', )

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ('name','code','marka','model',)
