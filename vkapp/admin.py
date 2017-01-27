from django.contrib import admin
from django.core.urlresolvers import reverse

from vkapp.forms import ProductSalesAdminForm, SalesAdminForm
from vkapp.models import Customer, Inventory, Sales, ProductSales


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_number','address']
    search_fields = ['name', 'contact_number']
    ordering = ['name']

    class Meta:
        model=Customer


class InventoryAdmin(admin.ModelAdmin):
    list_display = ['model_name', 'model_number', 'available_quantity', 'selling_price']
    search_fields = ['model_name', 'model_number']
    ordering = ['model_name']
    readonly_fields = ('available_quantity',)
    class Meta:
        model = Inventory


class ProductSalesAdmin(admin.TabularInline):
    form = ProductSalesAdminForm
    model = ProductSales
    extra = 1

    readonly_fields = ("get_selling_price","get_subtotal")


class SalesAdmin(admin.ModelAdmin):
    """
        exe autotodos check searchfields
        js cases -
        total updated when discount or subtotal changes
        update subtotal when qty changes
        do not allow to create if no available qty

    """
    form = SalesAdminForm
    list_display = ["get_customer_info", 'get_product_names', 'created_date', 'get_bill']
    search_fields = ['customer__contact_number', 'customer__name']
    inlines = (ProductSalesAdmin,)
    readonly_fields = ('total', )
    class Meta:
        model = Sales

    def get_customer_info(self, obj):
        return "%s : %s" % (obj.customer.name, str(obj.customer.contact_number))

    def get_product_names(self, obj):
        productlist = ''
        if obj.products:
            for prod in obj.productsales_set.all():
                productlist += "<span>"+str(prod.product) + " - " + str(prod.quantity) + " item(s)" + "</span><br>"
        return productlist

    def get_bill(selfself, obj):
        return '<a href="' + reverse('sales_pdf',kwargs={'sales_id':obj.pk}) + '">VIEW BILL</a>'

    get_bill.allow_tags = True
    get_product_names.allow_tags = True
    get_product_names.short_description = 'Products & Quantities'
    get_customer_info.short_description = 'Customer Info (Name:Contact_No)'

admin.site.register(Sales, SalesAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Inventory, InventoryAdmin)
