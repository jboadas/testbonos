from django.contrib.auth.models import User
from quickbonos.mainbonos.models import Bonos
from rest_framework import viewsets
from rest_framework import permissions
from quickbonos.mainbonos.serializers import (
    UserSerializer,
    BonosSerializer)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
import requests
from decimal import Decimal


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class BonosViewSet(viewsets.ModelViewSet):
    queryset = Bonos.objects.all()
    serializer_class = BonosSerializer
    permission_classes = [permissions.IsAuthenticated]

    def call_banxico_api(self):
        url = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718/datos/oportuno'
        headers = {
            "Accept": "application/json",
            "Bmx-Token": "998e9ae2587c2e90d01c616faad0fa854d14fee0ae00e48c44d4dbcf90612c12"
        }

        try:
            resp = requests.get(url=url, headers=headers)
        except Exception:
            return 0
        else:
            data = resp.json()
            series = data.get('bmx').get('series')
            if type(series) == list and len(series) > 0:
                datos = series[0].get('datos')
                if type(datos) == list and len(datos) > 0:
                    exchange_rate = datos[0].get('dato')
                    # exchange_date = datos[0].get('fecha')
                    try:
                        float_exch_rate = Decimal(exchange_rate)
                    except Exception:
                        return 0
                    else:
                        return float_exch_rate

    @action(detail=True, methods=['get'], url_path='comprabono')
    def compra_bono(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user.username)
        bono = super(BonosViewSet, self).get_object()
        if not bono.bought_by:
            bono.bought_by = user
            bono.save()
        custom_response = {"comprabono": request.user.id}
        return Response(custom_response, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'], url_path='preciousd')
    def precio_usd(self, request, *args, **kwargs):
        exchange_rate = self.call_banxico_api()
        if exchange_rate != 0:
            bono = super(BonosViewSet, self).get_object()
            price_usd = bono.bono_price / exchange_rate
            custom_response = {"USD": str(price_usd), "MXN": bono.bono_price}
            return Response(custom_response, status=status.HTTP_200_OK)
        else:
            custom_response = {"error": "cannot access banxico api"}
            return Response(
                custom_response,
                status=status.HTTP_424_FAILED_DEPENDENCY)
