from rest_framework import viewsets
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer
from .kafka_pducer import KafkaProduce
import uuid
from datetime import datetime

kafka_producer = KafkaProduce('transfer_topic')


class TransferViewSet(viewsets.ViewSet):
    queryset = Transaction.objects.all()

    def create(self, request):
        """POST api/transfers/
        {
            "from_account": "12345",
            "to_account": "67890",
            "amount": 1000.00
        }
        """
        transaction_id = str(uuid.uuid4())
        data = {
            'transaction_id': transaction_id,
            'status': 'PENDING',
            'measge': 'Transfer initiated successfully',
            'timestamp': datetime.now().isoformat()
        }

        kafka_producer.send(data)
        Transaction.objects.create(
            transaction_id=transaction_id,
            **request.data,
            status='PENDING',
        )
        return Response(data, status=201)
    
    def retrieve(self, request, pk=None):
        """
            GET api/transfers/12345"""
        transaction = Transaction.objects.get(transaction_id=pk)
        return Response({
            'transaction_id': transaction.transaction_id,
            'status': transaction.status,
            'message': 'Transfer initiated successfully',
            'timestamp': transaction.timestamp.isoformat()
        })
    
    def list_account_transactions(self, request):
        account_id = request.query_params.get('account_id')
        transactions = Transaction.objects.filter(from_account=account_id)
        return Response(TransactionSerializer(transactions, many=True).data)
