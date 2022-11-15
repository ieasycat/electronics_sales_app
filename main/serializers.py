from rest_framework.serializers import ModelSerializer, SlugRelatedField
from .models import ObjectRelationship, NetworkElement, Contact, Address, Product
from rest_framework import serializers


class ObjectRelationshipSerializer(ModelSerializer):
    object = SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = ObjectRelationship
        fields = ('object', 'type_object')


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'model', 'release_date')


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ('country', 'city', 'street', 'house_number')


class ContactSerializer(ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Contact
        fields = ('email', 'address')


class NetworkElementSerializer(ModelSerializer):
    contact = ContactSerializer()
    provider = ObjectRelationshipSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = NetworkElement
        fields = ('id', 'name', 'staff', 'debt', 'contact', 'provider', 'products', 'date_create')


class IndebtednessNetworkElementSerializer(ModelSerializer):
    provider = ObjectRelationshipSerializer()

    class Meta:
        model = NetworkElement
        fields = ('id', 'name', 'debt', 'provider')


class FilterProductNetworkElementSerializer(ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = NetworkElement
        fields = ('id', 'name', 'products')


class CreateProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UpdateProductSerializer(serializers.Serializer):
    network_elements = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=25, required=False)
    model = serializers.CharField(max_length=25, required=False)
    release_date = serializers.DateField(required=False)


class CreateNetworkElementSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    staff = serializers.CharField(max_length=255)
    debt = serializers.DecimalField(max_digits=8, decimal_places=2)
    email = serializers.EmailField()
    country = serializers.CharField(max_length=20)
    city = serializers.CharField(max_length=20)
    street = serializers.CharField(max_length=20)
    house_number = serializers.CharField(max_length=20)
    provider = serializers.IntegerField(required=False)


class UpdateNetworkElementSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, required=False)
    staff = serializers.CharField(max_length=255, required=False)
    debt = serializers.DecimalField(max_digits=8, decimal_places=2, read_only=True)
    email = serializers.EmailField(required=False)
    country = serializers.CharField(max_length=20, required=False)
    city = serializers.CharField(max_length=20, required=False)
    street = serializers.CharField(max_length=20, required=False)
    house_number = serializers.CharField(max_length=20, required=False)
    provider = serializers.IntegerField(required=False)
