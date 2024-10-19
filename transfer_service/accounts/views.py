from rest_framework import viewsets
from rest_framework.response import Response
from .models import Account
from datetime import datetime
from .serializers import AccountSerializer


class AccountViewSet(viewsets.ViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
    def retrieve(self, request, pk=None):
        """"
            GET accounts/12345
        """
        account = Account.objects.get(account_id=pk)
        return Response({
            'accountId': account.account_id,
            'balance': account.balance,
            'currency': account.currency,
            'timestamp': account.timestamp
        })
    
    def create(self, request):
        """POST
        {
            "account_id": "12345",
            "balance": 1000.00,
            "currency": "USD"
        }
        """
        account = Account.objects.create(**request.data)
        return Response({
            'accountId': account.account_id,
            'balance': account.balance,
            'currency': account.currency,
        })