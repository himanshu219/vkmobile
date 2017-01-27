from dal import autocomplete
from rest_framework.generics import RetrieveAPIView
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from models import Customer,Inventory, Sales
from vkapp.serializers import SalesSerializer


class CustomerAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # filtering on active customers and add Q support
        if not self.request.user.is_authenticated():
            return Customer.objects.none()

        qs = Customer.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

class ProductAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # filtering on available products and add Q support
        if not self.request.user.is_authenticated():
            return Inventory.objects.none()

        qs = Inventory.objects.all()

        if self.q:
            qs = qs.filter(model_name__istartswith=self.q)

        return qs


class SalesPdfView(RetrieveAPIView):
    lookup_field = 'id'
    lookup_url_kwarg = 'sales_id'
    renderer_classes = (JSONRenderer,TemplateHTMLRenderer)
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    template_name = "bill.html"
