from rest_framework import viewsets
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer
from .kafka_pducer import KafkaProduce
import uuid
from datetime import datetime

kafka_producer = KafkaProduce('transfer_topic')


class TransferViewSet(viewsets.ViewSet):
    def create(self, request):
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
    
    def retrieve(self, request, pk=None):
        transaction = Transaction.objects.get(transaction_id=pk)
        return Response({
            'transaction_id': transaction.transaction_id,
            'status': transaction.status,
            'message': 'Trasaction status retrieved',
            'timestamp': transaction.timestamp.isoformat()
        })
    
    def list_account_transactions(self, request):
        account_id = request.query_params.get('account_id')
        transactions = Transaction.objects.filter(from_account=account_id)
        return Response(TransactionSerializer(transactions, many=True).data)
