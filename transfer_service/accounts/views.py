from rest_framework import viewsets
from rest_framework.response import Response
from .models import Account
from datetime import datetime


class AccountViewSet(viewsets.ModelViewSet):
    """2й метод [POST] Пополнение текущего счета
        Пример запроса: [/accounts/{accountId}/deposit]
    {
        "amount": 200.00
        "currency": "USD"""

    def retrieve(self, request, pk=None):
        account = Account.objects.get(account_id=pk)
        return Response({
            'accountId': account.account_id,
            'balance': account.balance,
            'currency': account.currency,
            'timestamp': account.timestamp
        })
    
    def create(self, request):
        account = Account.objects.create(**request.data)
        return Response({
            'accountId': account.account_id,
            'balance': account.balance,
            'currency': account.currency,
        })