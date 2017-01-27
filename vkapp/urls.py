from django.conf.urls import patterns, include, url

from vkapp.api import CustomerAutocomplete, ProductAutocomplete, SalesPdfView

urlpatterns = patterns('',

           url(r'^customer-autocomplete/$', CustomerAutocomplete.as_view(), name='customer-autocomplete'),
           url(r'^product-autocomplete/$', ProductAutocomplete.as_view(), name='product-autocomplete'),
           url(r'^salespdf/(?P<sales_id>[-\w]+)/$', SalesPdfView.as_view(),
               name='sales_pdf'),
)
