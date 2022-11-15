from django.urls import path, include
from .views import APINetworkElementSet, APINetworkElementFiler, APIAverageDebtStatistics, \
    APINetworkElementFilerProduct, APICreateProduct, APICreateNetworkElement, \
    APIUpdateAndDeleteNetworkElement, APIProduct

urlpatterns = [
    path('network_elements/', APINetworkElementSet.as_view(), name='network_elements_list'),
    path('network_element/country/<str:country>/', APINetworkElementFiler.as_view(), name='network_element_filter'),
    path('average_debt_statistics/', APIAverageDebtStatistics.as_view(), name='average_debt_statistics'),
    path('network_element/product/<int:product_id>/', APINetworkElementFilerProduct.as_view(),
         name='network_element_filter_product'),
    path('create_product/', APICreateProduct.as_view(), name='create_product'),
    path('product/<int:pk>/', APIProduct.as_view(), name='update_and_delete_product'),
    path('create_network_element/', APICreateNetworkElement.as_view(), name='create_network_element'),
    path('network_element/<int:pk>/', APIUpdateAndDeleteNetworkElement.as_view(),
         name='update_and_delete_network_element'),
    path('api-auth/', include('rest_framework.urls'))
]
