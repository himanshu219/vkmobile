from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator, MaxLengthValidator, validate_integer


class Customer(models.Model):
    contact_number = models.CharField(max_length=15,
                                      validators=[MaxLengthValidator(10), MinLengthValidator(10), validate_integer],
                                      verbose_name="Mobile Number",unique=True,
                                      help_text="Please enter 10 digit mobile number only.")
    name = models.CharField(max_length=50, verbose_name="Customer Name",
                            help_text="Please enter the full name of the customer", validators=[MinLengthValidator(3)])
    address = models.TextField(blank=True, null=True, help_text="Please enter the full address of the customer")
    modify_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    def __unicode__(self):
        return "%s : %s" % (self.name,str(self.contact_number))

class Inventory(models.Model):
    model_number = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    total_quantity = models.IntegerField(default=0)
    available_quantity = models.IntegerField(default=0)
    selling_price = models.DecimalField(max_digits=11, decimal_places=2, default=0.0, help_text="Selling price per item")
    modify_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    def __unicode__(self):
        return "%s : %s" % (self.model_number, str(self.model_name))

    def save(self, *args, **kwargs):
        if not self.pk:
            self.available_quantity = self.total_quantity
        super(Inventory,self).save(*args, **kwargs)

class Sales(models.Model):
    customer = models.ForeignKey(Customer)
    products = models.ManyToManyField(Inventory, through="ProductSales")
    discount = models.IntegerField(default=0, help_text="Discount in Rupees")
    total = models.DecimalField(max_digits=11, decimal_places=2, default=0.0)
    modify_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        #calculate total after subtracting discount and subtract from available quantity
        self.total = self.total - self.discount
        super(Sales, self).save(*args, **kwargs)
        for obj in self.productsales_set.all():
            obj.product.available_quantity -= obj.quantity
            obj.product.save()




class ProductSales(models.Model):
    sales = models.ForeignKey(Sales)
    product = models.ForeignKey(Inventory)
    quantity = models.IntegerField(default=1)


    def get_selling_price(self):
        return self.product.selling_price


    def get_subtotal(self):
        return self.product.selling_price*self.quantity


    get_selling_price.short_description = 'Cost Per Item'
    get_subtotal.short_description = 'SubTotal'

