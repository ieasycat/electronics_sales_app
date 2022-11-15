from django.contrib import admin
from .models import *
from django.db.models import QuerySet


class ObjectRelationshipAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_object', 'get_object_name', 'get_network_element_name')
    list_display_links = ('id', 'get_object_name')
    list_per_page = 10
    list_filter = ('object__name', )

    @admin.display(description='Provider')
    def get_object_name(self, obj):
        return obj.object.name

    @admin.display(description='Buyer')
    def get_network_element_name(self, obj):
        return obj.provider.name


class NetworkElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_contact', 'staff', 'provider', 'debt', 'date_create')
    list_filter = ('contact__address__city',)
    list_display_links = ('id', 'name')
    list_per_page = 10
    actions = ('debt_clearing',)

    @admin.display(description='Contact details')
    def get_contact(self, obj):
        contact = obj.contact
        address = contact.address
        return f'{contact.email}\n ' \
               f'{address.country}, {address.city}, {address.street}, {address.house_number}'

    @admin.action(description='Clearing debts to the provider')
    def debt_clearing(self, request, qs: QuerySet):
        qs.update(debt=0)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'address')
    list_display_links = ('id', 'email')
    list_per_page = 10

    @admin.display(description='Address')
    def get_address(self, obj):
        address = obj.address
        return f'{address.country}, {address.city}, {address.street}, {address.house_number}'


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_email', 'country', 'city', 'street', 'house_number')
    list_display_links = ('id', 'country')
    list_per_page = 10

    @admin.display(description='Email')
    def get_email(self, obj):
        return obj.contact.email


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_supplier', 'name', 'model', 'release_date')
    list_display_links = ('id', 'name')
    list_per_page = 10

    @admin.display(description='Supplier')
    def get_supplier(self, obj):
        return obj.network_elements.name


admin.site.register(ObjectRelationship, ObjectRelationshipAdmin)
admin.site.register(NetworkElement, NetworkElementAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Product, ProductAdmin)
