from constructor.paginator import ResultsSetPagination
from rest_framework import viewsets
from constructor import models
from api.serializers import currency
from rest_framework.decorators import action
from rest_framework.response import Response


class CurrencyView(viewsets.ModelViewSet, ResultsSetPagination):
    queryset = models.Currency.objects.all()
    serializer_classes = {
        'list': currency.CurrencyListSerializer,
        'retrieve': currency.CurrencyListSerializer,
    }
    default_serializer_class = currency.CurrencyListSerializer
    pagination_class = ResultsSetPagination

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    @action(detail=False, methods=['get'], name='all', url_path='all')
    def states(self, request, *args, **kwargs):
        """
        Returns  states list by country id with count`.
        """
        qs = models.Currency.objects.all().order_by('description')
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
