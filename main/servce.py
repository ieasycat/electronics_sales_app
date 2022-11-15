from .models import NetworkElement
from decimal import Decimal


def average_debt() -> Decimal:
    count_objects = NetworkElement.objects.count()
    objects = NetworkElement.objects.all()
    avg_debt = 0

    for elem in objects:
        avg_debt += elem.debt

    return avg_debt / count_objects
