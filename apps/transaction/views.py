from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.models import Avg, Count, Max, ExpressionWrapper, F, CharField
import json
import datetime

from apps.base.views import (BaseView, LoginRequiredMixin)
from apps.ip.models import IP
from .models import Transaction


class TransactionStatusAPI(BaseView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, *args, **kwargs):
        result = {
            "data": [ 
            ]
        }

        try:
            your_ip = IP.objects.values_list('address', flat=True).filter(user_profile=self.request.user.profile)
            your_id_transaction = Transaction.objects.filter(address__in=set(your_ip)).values('address').annotate(id=Max('id')).values_list("id", flat=True)
            your_transaction = Transaction.objects.filter(id__in=set(your_id_transaction))
            
            #print("your_transaction: ", your_transaction)
            for transaction in your_transaction:
                arr_data = []
                arr_data.append(transaction.address)
                arr_data.append(transaction.agent_ping_time.strftime('%m/%d/%Y %H:%M:%S'))
                if transaction.time_avg == 999:
                    arr_data.append('Offline')
                else:
                    arr_data.append(transaction.time_avg)

                result['data'].append(arr_data)
        except Exception as error:
            print("Something error: ", error)

        return HttpResponse(json.dumps(result))


class TransactionAPI(BaseView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, *args, **kwargs):
        result = {
            "data": [ 
            ]
        }

        try:
            your_ip = IP.objects.values_list('address', flat=True).filter(user_profile=self.request.user.profile)
            your_transaction = Transaction.objects.filter(address__in=set(your_ip)).order_by('-id')
            for transaction in your_transaction:
                arr_data = []
                arr_data.append(transaction.address)
                arr_data.append(transaction.agent_ping_time.strftime('%m/%d/%Y %H:%M:%S'))
                arr_data.append(str(transaction.time_avg) + ' ms')

                result['data'].append(arr_data)
        except:
            print("Something error!")

        return HttpResponse(json.dumps(result))

    def post(self, *args, **kwargs):
        js_data = self.request.body.decode('utf-8')
        if self._insert_data(js_data):
            result = {'status': True}
        else:
            result = {'status': False}
        return HttpResponse(json.dumps(result))

    def _insert_data(self, receive):
        # {
        #     "data": b '[{"i": "192.168.1.1", "t": 77, "c": "2016-05-17 07:32:42"}, {"i": "192.168.1.2", "t": 22, "c": "2016-05-17 07:32:42"}, {"i": "192.168.1.3", "t": 97, "c": "2016-05-17 07:32:42"}]',
        #     'vhost': 'default'
        # }
        try:
            receive = json.loads(receive)
            list_data = receive['data']
            print("list_data: ", list_data)
            for item in list_data:
                print("item: ", item)
                transaction = Transaction()
                transaction.address = item['ip']
                transaction.vhost = receive['vhost']
                transaction.time_avg = float(str(item['t']))
                transaction.agent_ping_time = datetime.datetime.strptime(item['c'], "%Y-%m-%d %H:%M:%S")
                transaction.save()
            return True
        except Exception as error:
            print("Loi me no roi ", error)
            return False

