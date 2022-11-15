from .serializers import NetworkElementSerializer, IndebtednessNetworkElementSerializer, \
    FilterProductNetworkElementSerializer, CreateProductSerializer, \
    CreateNetworkElementSerializer, UpdateNetworkElementSerializer, UpdateProductSerializer
from .models import NetworkElement, Address, Contact, ObjectRelationship, Product
from rest_framework import generics, status
from .servce import average_debt
from rest_framework.response import Response


class APINetworkElementSet(generics.ListAPIView):
    queryset = NetworkElement.objects.all()
    serializer_class = NetworkElementSerializer


class APINetworkElementFiler(generics.ListAPIView):
    serializer_class = NetworkElementSerializer

    def get_queryset(self):
        country = self.kwargs['country']
        return NetworkElement.objects.filter(contact__address__country=country)


class APIAverageDebtStatistics(generics.ListAPIView):
    serializer_class = IndebtednessNetworkElementSerializer

    def get_queryset(self):
        return NetworkElement.objects.filter(debt__gte=average_debt())


class APINetworkElementFilerProduct(generics.ListAPIView):
    serializer_class = FilterProductNetworkElementSerializer

    def get_queryset(self):
        product = self.kwargs['product_id']
        return NetworkElement.objects.filter(products=product)


class APICreateProduct(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer


class APIProduct(generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = UpdateProductSerializer

    def put(self, request, pk: int):
        product = Product.objects.get(pk=pk)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        product.name = validated_data.get('name', product.name)
        product.model = validated_data.get('model', product.model)
        product.network_elements = NetworkElement.objects.get(
            pk=validated_data.get('network_elements', product.network_elements_id))
        product.release_date = validated_data.get('release_date', product.release_date)

        product.save()
        return Response({'success': 'Successfully update Product'}, status=status.HTTP_200_OK)

    def delete(self, request, pk: int):
        Product.objects.get(pk=pk).delete()
        return Response({'success': 'Successfully delete Product'}, status=status.HTTP_200_OK)


class APICreateNetworkElement(generics.GenericAPIView):
    serializer_class = CreateNetworkElementSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        address = Address.objects.create(
            country=validated_data.get('country'),
            city=validated_data.get('city'),
            street=validated_data.get('street'),
            house_number=validated_data.get('house_number'),
        )
        contact = Contact.objects.create(email=validated_data.get('email'), address=address)
        NetworkElement.objects.create(
            name=validated_data.get('name'),
            contact=contact,
            provider=ObjectRelationship.objects.get(pk=validated_data.get('provider')) if
            validated_data.get('provider') else None,
            staff=validated_data.get('staff'),
            debt=validated_data.get('debt')
        )
        return Response({'success': 'Successfully added Network Element'}, status=status.HTTP_201_CREATED)


class APIUpdateAndDeleteNetworkElement(generics.GenericAPIView):
    queryset = NetworkElement.objects.all()
    serializer_class = UpdateNetworkElementSerializer

    def put(self, request, pk):
        network_element = NetworkElement.objects.get(pk=pk)
        contact_network_element = Contact.objects.filter(network_element=network_element).first()
        address_network_element = Address.objects.filter(contact=contact_network_element).first()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        network_element.name = validated_data.get('name', network_element.name)
        network_element.staff = validated_data.get('staff', network_element.staff)

        contact_network_element.email = validated_data.get('email', contact_network_element.email)

        address_network_element.country = validated_data.get('country', address_network_element.country)
        address_network_element.city = validated_data.get('city', address_network_element.city)
        address_network_element.street = validated_data.get('street', address_network_element.street)
        address_network_element.house_number = validated_data.get('house_number', address_network_element.house_number)

        network_element.provider = ObjectRelationship.objects.get(
            pk=validated_data.get('provider', network_element.provider_id))

        network_element.save()
        contact_network_element.save()
        address_network_element.save()
        return Response({'success': 'Successfully update Network Element'}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        NetworkElement.objects.get(pk=pk).delete()
        return Response({'success': 'Successfully delete Network Element'}, status=status.HTTP_200_OK)
