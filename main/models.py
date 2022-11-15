from django.db import models


class ObjectRelationship(models.Model):
    type_network_element_list = (
        ('Завод', 'Завод'),
        ('Дистрибьютор', 'Дистрибьютор'),
        ('Дилерский центр', 'Дилерский центр'),
        ('Крупная розничная сеть', 'Крупная розничная сеть'),
        ('Индивидуальный предприниматель', 'Индивидуальный предприниматель')
    )

    object = models.OneToOneField(
        'NetworkElement',
        null=False,
        on_delete=models.CASCADE,
        related_name='object'
    )
    type_object = models.CharField(max_length=255, choices=type_network_element_list, verbose_name='Type provider')

    def __str__(self):
        return f'{self.type_object} {self.object.name}'


class NetworkElement(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name of the object')
    contact = models.OneToOneField(
        'Contact',
        null=False,
        on_delete=models.CASCADE,
        related_name='network_element',
        verbose_name='Contact details'
    )
    provider = models.OneToOneField(
        'ObjectRelationship',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='provider'
    )
    staff = models.CharField(max_length=255, verbose_name='Staff')
    debt = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Debt')
    date_create = models.DateField(auto_now_add=True, verbose_name='Date of creation')

    def __str__(self):
        return f'{self.pk}: ' \
               f'{self.name}, {self.contact}, {self.staff}, {self.debt}, {self.date_create}'

    class Meta:
        verbose_name = 'Network object'
        verbose_name_plural = 'Network objects'


class Contact(models.Model):
    email = models.EmailField(unique=True)
    address = models.OneToOneField(
        'Address',
        null=True,
        on_delete=models.CASCADE,
        related_name='contact'
    )

    def __str__(self):
        return f'{self.email}: {self.address}'


class Address(models.Model):
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=50, db_index=True)
    street = models.CharField(max_length=50)
    house_number = models.CharField(max_length=10, db_index=True)

    def __str__(self):
        return f'{self.country}, {self.city}, {self.street}, {self.house_number}'


class Product(models.Model):
    network_elements = models.ForeignKey(
        'NetworkElement',
        null=False,
        on_delete=models.CASCADE,
        related_name='products'
    )
    name = models.CharField(max_length=25, db_index=True)
    model = models.CharField(max_length=25, db_index=True)
    release_date = models.DateField()

    def __str__(self):
        return f'{self.network_elements.name}, {self.name}, {self.model}, {self.release_date}'
