from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
import json
from .serializers import StockSerializer

#List all stocks or create new

class StockList(APIView):

    def get(self,request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks,many=True)
        return Response(serializer.data)
    def post(self,request):
        param = request.query_params
        pa = json.dumps(param)
        json_response = json.loads(pa)
        print(json_response["ticker"]+"")
        s=Stock()
        s.ticker = json_response["ticker"]+""
        s.opens= float(json_response["opens"])
        s.close= float(json_response["close"])
        s.volume= int(json_response["volume"])
        s.save()
        return Response("lol")
