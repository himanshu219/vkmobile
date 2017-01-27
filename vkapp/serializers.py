from rest_framework import serializers

from vkapp.models import Sales, Customer, Inventory,  ProductSales



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id', 'model_number', 'model_name', 'selling_price')

class ProductSalesSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer(read_only=True)
    subtotal = serializers.SerializerMethodField(source='subtotal')
    class Meta:
        model = ProductSales
        fields = ('product', 'quantity','subtotal')

    def get_subtotal(self, obj):
        return obj.get_subtotal()

    def to_representation(self, instance):
        data = super(ProductSalesSerializer, self).to_representation(instance)
        product = data.pop('product')
        for k,v in product.items():
            data['product_'+k] = v
        return data

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'address', 'contact_number')

class SalesSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    products = ProductSalesSerializer(read_only=True, many=True, source='productsales_set')
    total_without_discount = serializers.SerializerMethodField()

    class Meta:
        model = Sales
        fields = ('id','created_date', 'discount', 'total', 'customer', 'products', 'total_without_discount')

    def get_total_without_discount(self, obj):
        return sum([p.get_subtotal() for p in obj.productsales_set.all()])



